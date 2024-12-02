import mysql.connector
from utilities.configurations import *

# connect function expects 4 fields to connect to db:
# host, database, username, password

# connection = mysql.connector.connect(host='localhost', database='PythonAutomation',
#                         user='root', password='root')

connection = getConnection()

print(connection.is_connected()) # True if connected , False if not

cursor = connection.cursor() # To create a stream between db and python in order to run queries
cursor.execute('select * from CustomerInfo')

all_rows = cursor.fetchall()  # To fetch all records in table
row = cursor.fetchone()  # To fetch 1st record in table

# row will be in tuple
print(row)  # Output = ('selenium', datetime.date(2020, 6, 7), 120, 'Africa')
print(row[3])  # Output = 'Africa'

rowAll = cursor.fetchall()
print(rowAll)  # output will be in list not tuple , tuple for only one record
# output = [('Protractor', datetime.date(2020, 6, 7), 45, 'Africa'), ('Appium', datetime.date(2020, 6, 7), 99,
# 'Asia')]

# fetch will be done after where cursor is last used

# Iterate and add the sum of every record from the sum column after fetching all
rows = cursor.fetchall()
sum_total = 0
for row in rows:  # every iteration will give sth like this: ('Protractor', datetime.date(2020, 6, 7), 45, 'Africa')
    sum_total += row[2]
assert sum_total == 361

print(sum_total)

# SET SQL_SAFE_UPDATES = 0
# update customerInfo set Location = 'US' where CourseName = 'Jmeter'
query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK","Jmeter")
cursor.execute(query, data)  # This will use data in the query while executing

connection.commit() # commit should happen on connection level and not cursor level

delete_query = "delete from customerInfo where courseName = %s"
delete_courseName = "WebServices"
cursor.execute(delete_query,delete_courseName)
connection.commit()


connection.close()  # close connection at end of script
