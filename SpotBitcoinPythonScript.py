#This script gets the current SPOT BTC in USD from Coinbase. 
#Documentaiton https://docs.cloud.coinbase.com/sign-in-with-coinbase/docs/api-prices

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
print(spot_price) ###CODE WORKS UP TO THIS POINT, 3/23/24

##**lEAVING THIS HERE, INSTRUCTIONS ON HOW THE CSV MODULE, AND WRITE USING A DICTIONARY TO A CSV
#Source Below
#https://www.geeksforgeeks.org/working-csv-files-python/


# my data rows as dictionary objects
mydict = spot_price ###THIS VARIABLE NEEDS TO BE FIXED AS A PROPER DICTIONARY. THIS CODE CREATES A CSV. :)

# field names
fields = ['amount', 'base', 'year', 'currency']

# name of csv file
filename = "current_spot_price_btc.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames=fields)

	# writing headers (field names)
	writer.writeheader()

	# writing data rows
	writer.writerows(mydict)
