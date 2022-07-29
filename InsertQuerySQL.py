import SqlConnect as util

def insertData(row):
    conn = util.get_connection()
    mysql_cursor = conn.cursor()
    mysql_cursor.execute("INSERT INTO SedapData(EntryID , CustID, CustFirstName, CustLastName, ChannelNo, StartWatchTime, EndWatchTime, CustomearAge) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    conn.commit()
    util.close_connection(conn)

def checkData():
    pass
