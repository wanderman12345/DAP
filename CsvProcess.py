import csv
from multiprocessing.sharedctypes import Value
from InsertQuerySQL import *
from ActiveMQConnect import *
from ValidationData import *

# Open CSV File and Read Data then send data to validation

file = open("/Users/mathewraju/Desktop/CustomerWatchTime_04072020.csv")
csvreader = csv.reader(file)
header = []
header = next(csvreader)
unique = set()
error = False
fileWrite = open('Error.csv',  'w')
writer = csv.writer(fileWrite)

for row in csvreader:
    try:
        checkElementID(row, unique)
        checkCustomerID(row)
        checkCustomerFirstName(row)
        checkCustomerLastName(row)
        checkChannelNumber(row)
        checkStartWatchTime(row)
        checkEndWatchTime(row)
        checkCustomerAge(row)

    except ValueError:
        error = True
        writer.writerow(row)

        print(row)
        print("This row has invalid value(s) and will be sent to ActiveMQ")



    else:
        # If all data is valid then send each row to mySQL server
        insertData(row)
        checkData()

if error:
        fileWrite.close()
        fileWrite = open('Error.csv', 'r')
        sendMessageActiveMQ(fileWrite)






