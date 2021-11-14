import mysql.connector

# It connects you to your Server
myb = mysql.connector.connect(host="localhost", user="root", passwd="KANISHA*23")

# Returns Object of your Server through which we can modify it
mycursor = myb.cursor()

# It executes the statement
mycursor.execute("CREATE DATABASE Restaurant_Management")