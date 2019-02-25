# Politics Upload

## Project Description  

For this project, we will be downloading all of the electronic files from the Federal Election Commission submitted by the Beto for Texas Senate campaign in 2018. Work was done using Python and dependencies: Pandas, SQLalchemy, and Flask.   

Beto O’Rourke, the Democratic candidate for U.S. Senate in Texas in 2018 raised more money than any candidate for Senate in history — more than $70 million.    

http://time.com/money/5440193/beto-campaign-money-map-midterms/  

To start, we will be extracting the raw data from the FEC website and Gov’t S3 buckets by running a loop through the downloaded CSV files and inputting the information into two Pandas Dataframes, differentiated by FEC and AWS sources.

From there, the data was concatenated into one dataframe. After this step, the single dataframe was uploaded to a SQLite database named "contributions". The database features information including individual donor names, as disbursements were removed, and donor address, city, state, zip, employer, occupation and the total amount donated to the campaign.

In addition to this database, a Flask application is available to easily traverse the data and locate individual names and top donors to the campaign.   

Campaigns for U.S. Senate are required to submit paper filings on a quarterly schedule that depends on when primary and general elections are held. We referenced the schedule here to see which filings we would need to download to get a complete list of Beto for Texas donors (https://transition.fec.gov/info/report_dates_2018.shtml#quarterly).   

## Future Work and Improvements

A possible future project regarding this data could include pulling information from the Whitepages API in conjecture to the available addresses. This could provide information ranging from the age of various donors to their marital status. 

It would also be valuable to present the date in a more uniform format as this would allow further search features within our FLASK API. 


### Data Sources    

1. Gov’t AWS S3 for FEC  
	main url:  https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/index.html  
2. fec.gov website  
	main url: https://www.fec.gov/data/committees/  


APRIL QUARTERLY 2017  
FEC file number	FEC-1159935  
Report coverage	January 1, 2017 to March 31, 2017  
source: https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/paper/20170421.zip  

JULY QUARTERLY 2017  
FEC file number	FEC-1173281  
Report coverage	April 1, 2017 to June 30, 2017  
source: https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/paper/20170719.zip  

OCTOBER QUARTERLY 2017  
FEC file number	FEC-1189361  
Report coverage	July 1, 2017 to September 30, 2017  
source: https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/paper/20171024.zip  

YEAR-END 2017  
FEC file number	FEC-1207075  
Report coverage	October 1, 2017 to December 31, 2017  
source: https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/paper/20180207.zip  

PRE-PRIMARY 2018  
FEC file number	FEC-1211345  
Report coverage	January 1, 2018 to February 14, 2018  
source: https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/paper/20180224.zip  

APRIL QUARTERLY 2018  
FEC file number	FEC-1226370  
Report coverage	February 15, 2018 to March 31, 2018  
source: https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/paper/20180420.zip  

JULY QUARTERLY 2018  
FEC file number	FEC-1290651  
Report coverage	April 1, 2018 to June 30, 2018  
source: http://docquery.fec.gov/csv/651/1290651.csv  

OCTOBER QUARTERLY 2018  
FEC file number	FEC-1272768  
Report coverage	July 1, 2018 to September 30, 2018
source: http://docquery.fec.gov/csv/768/1272768.csv  

PRE-GENERAL 2018  
FEC file number	FEC-1284518  
Report coverage	October 1, 2018 to October 17, 2018  
source: http://docquery.fec.gov/csv/518/1284518.csv  


The data files above have been downloaded and saved to `data` folder in our repo.  
