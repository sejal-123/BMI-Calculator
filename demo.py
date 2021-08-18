import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abc456",
  database="internship"
)

mycursor = mydb.cursor()

sql = "INSERT INTO patient (name, age, phone, gender, bmi, date) VALUES('%s', '%d', '%s', '%s', '%d', '%s');"
val = ("sejal", 20, "7894561230", "f", 22, datetime.datetime.now());
mycursor.execute(sql % val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

