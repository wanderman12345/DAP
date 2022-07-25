import stomp
import csv

# Sending message
def sendMessageActiveMQ(CSV):
    csvreader = csv.reader(CSV)
    host = "localhost"
    port = 61613
    dest_queue = "/queue/SEDAP.MANUAL.ANALYSIS.QUEUE"
    message_body =  ""
    for eachRow in csvreader:
         message_body = message_body + str(eachRow) + '\n'

    conn = stomp.Connection(host_and_ports=[(host,port)])
    conn.connect()
    conn.send(destination=dest_queue ,body=message_body, persistent = 'true')
    conn.disconnect()





















