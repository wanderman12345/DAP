import csv
from multiprocessing.sharedctypes import Value
from ValidationData import *

# Open CSV File and Read Data then send data to validation

file = open("/Users/mathewraju/Desktop/CustomerWatchTime_04072020.csv")
csvreader = csv.reader(file)
header = []
header = next(csvreader)
unique = {}

for row in csvreader:
    try:
        checkElementID(row, unique)
        checkCustomerID(row)
        checkCustomerFirstName(row)
        checkCustomerLastName(row)
        checkStartWatchTime(row)
        checkEndWatchTime(row)
        checkChannelNumber(row)
        checkCustomerAge(row)
        # If all data is valid then send each row to mySQL server

    except ValueError:
        print("This row is invalid and will be sent to ActiveMQ")










































