#!/usr/bin/env python3

# Dependencies
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from os import listdir
from os.path import isfile, join
import glob

# load csv files collected from Gov't S3 bucket
aws_path = 'data/aws-s3'
aws_files = glob.glob(aws_path + "/*.csv")

# create a list of dataframes from the csv files
aws_list_df = []
for x in aws_files:
# set no header and skip first two rows, as we do not use these rows
    df = pd.read_csv(x, header=None, error_bad_lines=False, skiprows=2)
    aws_list_df.append(df)

# concatenate dataframes from aws s3 files into single aws_df
aws_df = pd.concat(aws_list_df, axis=0, ignore_index=True)

# create new dataframe with only the columns we need from aws_df
new_aws_df = aws_df[[0,2,3,4,5,8,9,10,11,12,13,15,16,17,19,20,21]].copy()
new_aws_df = new_aws_df.rename(columns = { 0: "schedule",
                             2: "pac",
                             3: "last_name",
                             4: "first_name",
                             5: "mi",
                             8: "address_1",
                             9: "address_2",
                             10: "city",
                             11: "state",
                             12: "zip_code",
                             13: "contrib_date",
                             15: "employer",
                             16: "occupation",
                             17: "contrib_cycle",
                             19: "contrib_itemize",
                             20: "contrib_agg",
                             21: "conduit"})

# keep only SA11AI (individual contributions) in our new_aws_df dataframe
new_aws_df = new_aws_df.query("schedule == 'SA11AI'")

# remove duplicate rows created by conduit contributions (mostly ActBlue)
new_aws_df = new_aws_df.query("conduit != 'X'")

print(new_aws_df.head())
print(new_aws_df.shape)

# load csv files collected from fec.gov website
fec_path = 'data/fec-gov'
fec_files = glob.glob(fec_path + "/*.csv")

# create a list of dataframes from the csv files
fec_list_df = []
for x in fec_files:
# set no header and skip first two rows, as we do not use these rows
    df = pd.read_csv(x, header=None, error_bad_lines=False, skiprows=2)
    fec_list_df.append(df)

# concatenate dataframes from fec.gov files into single fec_df
fec_df = pd.concat(fec_list_df, axis=0, ignore_index=True)

# create new dataframe with only the columns we need from fec_df
new_fec_df = fec_df[[0,6,7,8,9,12,13,14,15,16,19,23,24,17,20,21,26]].copy()
new_fec_df = new_fec_df.rename(columns = { 0: "schedule",
                             6: "pac",
                             7: "last_name",
                             8: "first_name",
                             9: "mi",
                             12: "address_1",
                             13: "address_2",
                             14: "city",
                             15: "state",
                             16: "zip_code",
                             19: "contrib_date",
                             23: "employer",
                             24: "occupation",
                             17: "contrib_cycle",
                             20: "contrib_itemize",
                             21: "contrib_agg",
                             26: "conduit"})

# keep only SA11AI (individual contributions) in our new_fec_df dataframe
new_fec_df = new_fec_df.query("schedule == 'SA11AI'")

# remove duplicate rows created by conduit contributions (mostly ActBlue)
new_fec_df = new_fec_df.loc[new_fec_df['conduit'].isnull()]

print(new_fec_df.head())
print(new_fec_df.shape)

# now we combine the two tables
combined_df = pd.concat([new_fec_df, new_aws_df], axis=0, ignore_index=True)
print(combined_df.shape)


# ADD CODE FOR LOADING INTO SQLITE

# Create our database engine
engine = create_engine('sqlite:///contributions.sqlite')

Base = declarative_base()

class Contributions(Base):
    __tablename__ = 'contributions'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    schedule= Column(String)
    pac= Column(String)
    last_name= Column(String)
    first_name= Column(String)
    mi= Column(String)
    address_1= Column(String)
    address_2= Column(String)
    city= Column(String)
    state= Column(String)
    zip_code = Column(Integer)
    contrib_date= Column(String)
    employer= Column(String)
    occupation= Column(String)
    contrib_cycle= Column(String)
    contrib_itemize= Column(Integer)
    contrib_agg= Column(Integer)
    conduit= Column(String)

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
session = Session(bind=engine)

# load the combined_df dateframe into SQLite in chunks of 200
combined_df.to_sql('contributions', con=engine, if_exists='append', index=False, chunksize=200)

# count and print the number of rows in SQL table
row_count = pd.read_sql("Select COUNT(*) from contributions", con=engine)
print(row_count)
