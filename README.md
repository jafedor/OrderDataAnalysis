# OrderDataAnalysis

This is a Python program I wrote myself for my own personal practice with a variety of concepts. 

The concepts I demonstrate in this program (in order) are the following:
  1) Using GitHub's API to download repo content by making an HTTP GET request
  2) Extracting from a zip file
  3) File reading and writing
  4) Using the Pandas Python module to grab data from an Excel spreadsheet and parse it
  5) Using dictionaries and loops to process & analyze data

-------------------------------------------------

The Excel spreadsheet in this repo (named ItemOrderData.xlsx) contains information on hypothetical
"orders" that various random people placed for certain office items. I got the mock spreadsheet
from https://www.contextures.com/xlsampledata01.html.

The sheet tracks 7 attributes for each order placed:
  1) the date the order was placed
  2) the region the order originated from
  3) the name of the person who placed the order
  4) the item ordered
  5) the number of units ordered
  6) the cost per unit for the order
  7) the total money value of the order
  
-------------------------------------------------

The purpose of this program is to get the Excel data from this GitHub repo, store it,
read the spreadsheet into a Pandas dataframe, and then perform some analyses on it. 
The two questions I chose to explore and answer with my code are 
  1) "Who spent the most money in total?"
  2) "What was the most popular item ordered in each region?" 
     (with popularitiy being defined as having the highest number of units purchased for all time).
The answers to both questions are printed out in the console.
