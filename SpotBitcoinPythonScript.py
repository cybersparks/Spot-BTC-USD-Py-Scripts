#This script gets the current SPOT BTC in USD from Coinbase and creates a CSV called "Spot_BTC_Price.csv" on your computer. 
#Documentaiton https://docs.cloud.coinbase.com/sign-in-with-coinbase/docs/api-prices

from itertools import count
import requests #Can handle HTTP requests / Can query data from websites
import json #JSON file parser library
import csv # importing the csv module

#variable storing coinbase API URL in python Format
url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

#requests.get function, send the http request using url variable
response = requests.get(url)

#Process with the JSON loads function
spot_price = json.loads(response.text)
#show spot btc price
print(spot_price) 

#INSTRUCTIONS ON HOW THE CSV MODULE, AND WRITE USING A DICTIONARY TO A CSV
#https://www.geeksforgeeks.org/working-csv-files-python/

# my data rows as dictionary objects
mydict = [spot_price]

# field names
fields = ['data', 'amount', 'base', 'currency'] #Had to use DATA as that is how the Coinbase API returns the dictionary.

# name of csv file
filename = "Spot_BTC_Price.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames=fields)

	# writing headers (field names)
	writer.writeheader()

	# writing data rows
	writer.writerows(mydict)

#To find the CSV created Search: c drive C:\Users\yourusername, for "Spot_BTC_Price.csv"

