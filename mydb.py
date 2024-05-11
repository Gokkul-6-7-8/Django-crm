import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Welcome@123',
)
# Go and create a database in mysql workbench

cursorObject=database.cursor()
print("All done!")