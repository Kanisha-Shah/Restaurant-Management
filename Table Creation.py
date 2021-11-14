import mysql.connector

myb = mysql.connector.connect(host="localhost", user="root", passwd="KANISHA*23", database="Restaurant_Management")

mycursor = myb.cursor()

#Creating table from query
mycursor.execute("CREATE TABLE Customer (Fname varchar(20) Not Null, lname varchar2(20) Not Null , custid int primary key,emailid not null varchar2(20) check(emailid like '%@%.com'),city varchar2(20) default 'Ahmedabad',street not null varchar2(20),pincode integer not null check(count = 6),gender not null varchar2(1) check(gender = 'F' or gender = 'M' or gender = 'O'), phoneno not null integer check(count =10),allergy varchar2(20) default 'Null')")

myb.commit()
