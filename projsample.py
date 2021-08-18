from tkinter import *
from datetime import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import mysql.connector
from pymysql import *
import xlwt
import pandas.io.sql as sql
import csv


root = Tk()
root.title("BMI calculator")
root.geometry("600x500+400+200")
root.configure(background = "sky blue")

def f1():
	root1.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	root1.withdraw()

def f3():
	conv.deiconify()
	root1.withdraw()

def f4():
	root1.deiconify()
	conv.withdraw()

def f5():
	patdata.delete(1.0,END)
	vipt.deiconify()
	root.withdraw()
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="abc456",
	database="internship"
	)

	mycursor = mydb.cursor()
	info = ""
	mycursor.execute("SELECT * FROM patient")

	myresult = mycursor.fetchall()
	
	for x in myresult:
		patdata.insert(INSERT, "NAME : " + str(x[1]) + "\n" + "AGE : " + str(x[2])+ "\n" + "PHONE : " + str(x[3]) +"\n"+ "GENDER : " + str(x[4]) + "\n" + "BMI : " + str(x[5]) + "\n\n\n")	
	

def f6():
	root.deiconify()
	vipt.withdraw()
	

def expo():
	con=connect(user="root",password="abc456",host="localhost",database="internship")
	cursor = con.cursor()
	query = "SELECT * FROM patient"
	cursor.execute(query)
	fname = "patient" + str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".csv"
	with open(fname,'w') as f:
		writer = csv.writer(f)
		for row in cursor.fetchall():
			writer.writerow(row)

	
def calculate():
	try:	
		name = entname.get()
		if name == "":
			raise Exception("name cannot be empty")
		if (name.isalpha())!=True:
			entname.delete(0,END)
			raise Exception("name should have alphabets")
		if len(name)<2:
			entname.delete(0,END)
			raise Exception("name should have atleast 2 characters")
	
		try:
			age=int(entage.get())
			if age<=0:
				entage.delete(0,END)
				raise Exception ("age should be a natural no")
			if age == "":
				entage.delete(0, END)
				raise Exception("invalid age")
		except ValueError:
			showerror("Error","your age is invalid ")
			entage.delete(0,END)
			return

		try : 
			phone = int(entphone.get())
			if phone <= 0:
				entPHONE.delete(0,END)
				raise Exception ("sorry !! invalid phone")
			if phone == "":
				entphone.delete(0, END)
				raise Exception("invalid phone")
			if len(str(phone)) != 10:
				entphone.delete(0, END)
				raise Exception("phone no should be 10 digits long")
		
		except ValueError:
			showerror("Error","your phone is invalid ")
			entphone.delete(0,END)
			return	 
	
		try:
			height=float(entheight.get())
			if height<=0:
				entheight.delete(0,END)
				raise Exception ("height should be a natural no")
			if height == "":
				entage.delete(0, END)
				raise Exception("invalid height")
		except ValueError:
			showerror("Error","your height is invalid ")
			entheight.delete(0,END)
			return

		try:
			weight=float(entweight.get())
			if weight<=0:
				entweight.delete(0,END)
				raise Exception ("weight should be a natural no")
			if weight == "":
				entage.delete(0, END)
				raise Exception("invalid weight")
		except ValueError:
			showerror("Error","your weight is invalid ")
			entweight.delete(0,END)
			return
		bmi = weight / height ** 2
		if bmi < 18.5:
			msgbmi = "You are underweight. "
		elif bmi > 18.5 and bmi < 25:
			msgbmi = "You are normal. "
		else:
			msgbmi = "You are overweight. "
		gender = s.get()
		if gender == 1:
			gen = "m"
		else:
			gen = "f"
		message = "Name : " + name + " Age : " + str(age) + " Phone : " + str(phone) + " Height : " + str(height) + " Weight : " + str(weight) + "\nBMI : " + str(bmi) + "\n"+msgbmi
		showinfo("Message", message)
		mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="abc456",
		database="internship"
		)

		mycursor = mydb.cursor()

		sql = "INSERT INTO patient (name, age, phone, gender, bmi, date) VALUES('%s', '%d', '%s', '%s', '%f', '%s');"
		val = (name, age, phone, gen, bmi, datetime.now());
		mycursor.execute(sql % val)
		'''Change in code'''
		mycursor.execute("SELECT count(*) from patient")
		cnt = mycursor.fetchone()[0]
		cntlabel.config(text = "Count = "+ str(cnt), font = ("arial", 18, "bold"))
		mydb.commit()
		mydb.close()
		

		
	except Exception as e:
		showerror("Error","issue " + str(e))
	else:
		entage.delete(0,END);		entname.delete(0,END);		entphone.delete(0, END);	
		entheight.delete(0, END);	entweight.delete(0, END);

def convert():
	try:
		try:
			heightf=float(entheightf.get())
			if heightf<=0:
				entheightf.delete(0,END)
				raise Exception ("height should be a natural no")
			if heightf == "":
				entheightf.delete(0, END)
				raise Exception("invalid height")
		except ValueError:
			showerror("Error","your height in feet is invalid ")
			entheightf.delete(0,END)
			return
		
		try:
			heightin=float(entheightin.get())
			if heightin<=0:
				entheightin.delete(0,END)
				raise Exception ("height should be a natural no")
			if heightin == "":
				entheightin.delete(0, END)
				raise Exception("invalid height")
		except ValueError:
			showerror("Error","your height in inches is invalid ")
			entheightin.delete(0,END)
			return
		height = heightf * 0.3048 + heightin * 0.0254
		message = "your height in metres is : " + str(height)
		showinfo("Message", message)
	except Exception as e:
		showerror("Error","issue " + str(e))
	else:
		entheightf.delete(0,END);		
		entheightin.delete(0,END);
	
	
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abc456",
  database="internship"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT count(*) from patient")
cnt = mycursor.fetchone()[0]
mydb.commit()
mycursor.close()
mydb.close()

datelabel = Label(root, text = datetime.now(), font = ("arial", 18, "bold"))
datelabel.pack(pady = 10)
calcbutton = Button(root, text = "Calculate BMI", font = ("arial", 18, "bold"), command = f1)
calcbutton.pack(pady = 10)
histbutton = Button(root, text = "View History", font = ("arial", 18, "bold"), command = f5)
histbutton.pack(pady = 10)
expobutton = Button(root, text = "Export data", font = ("arial", 18, "bold"), command = expo)
expobutton.pack(pady = 10)
global cntlabel
cntlabel = Label(root, text = "Count = "+ str(cnt), font = ("arial", 18, "bold"))
cntlabel.pack(pady = 10)

root1 = Toplevel(root)
root1.title("Calculate")
root1.geometry("700x500+400+200")
root1.configure(background = "pink")
root1.withdraw()

name = Label(root1, text = "Enter name", font = ("arial", 18, "bold"))
name.place(x = 10, y = 10)
entname = Entry(root1, bd = 5, font = ("arial", 18))
entname.place(x = 250, y = 10)

age = Label(root1, text = "Enter age", font = ("arial", 18, "bold"))
age.place(x = 10, y = 60)
entage = Entry(root1, bd = 5, font = ("arial", 18))
entage.place(x = 250, y = 60)

phone = Label(root1, text = "Enter phone", font = ("arial", 18, "bold"))
phone.place(x = 10, y = 110)
entphone = Entry(root1, bd = 5, font = ("arial", 18))
entphone.place(x = 250, y = 110)

s = IntVar()
gender = Label(root1, text = "Gender", font = ("arial", 18, "bold"))
gender.place(x = 10, y = 160)
mradio = Radiobutton(root1, text = "Male", font = ("arial", 18, "bold"), variable = s, value = 1)
mradio.place(x = 250, y = 160)
wradio = Radiobutton(root1, text = "Female", font = ("arial", 18, "bold"), variable = s, value = 2)
wradio.place(x = 360, y = 160)

height = Label(root1, text = "Enter height(m)", font = ("arial", 18, "bold"))
height.place(x = 10, y = 210)
entheight = Entry(root1, bd = 5, font = ("arial", 18))
entheight.place(x = 250, y = 210)

convertbtn = Button(root1, text = "Convert", font = ("arial", 18, "bold"), command = f3)
convertbtn.place(x= 550, y = 210) 

weight = Label(root1, text = "Enter weight(kg)", font = ("arial", 18, "bold"))
weight.place(x = 10, y = 260)
entweight = Entry(root1, bd = 5, font = ("arial", 18))
entweight.place(x = 250, y = 260)

backbutton = Button(root1, text = "Back", font = ("arial", 18, "bold"), command = f2)
backbutton.place(x = 10, y = 310)
calcbutton = Button(root1, text = "Calculate", font = ("arial", 18, "bold"), command = calculate)
calcbutton.place(x = 250, y = 310)



vipt=Toplevel(root)
vipt.title("View Records")
vipt.geometry("500x500+400+200")
vipt.configure(background="#dbe2ef")
vipt.withdraw()

patdata=ScrolledText(vipt,width=45, height=25)
btnvback=Button(vipt,text="Back", font=("arial",18,"bold"),command=f6)

patdata.pack(pady=5)
btnvback.pack(pady=5)



conv = Toplevel(root1)
conv.title("Convert")
conv.geometry("500x500+400+200")
conv.configure(background = "sky blue")
conv.withdraw()

heightf = Label(conv, text = "Enter height in feet", font = ("arial", 18, "bold"))
heightf.pack(pady = 20)
entheightf = Entry(conv, bd = 5, font = ("arial", 18))
entheightf.pack(pady = 20)

heightin = Label(conv, text = "Enter height in inches", font = ("arial", 18, "bold"))
heightin.pack(pady = 20)
entheightin = Entry(conv, bd = 5, font = ("arial", 18))
entheightin.pack(pady = 20)

backbutton = Button(conv, text = "Back", font = ("arial", 18, "bold"), command = f4)
backbutton.place(x = 150, y = 310)
convbutton = Button(conv, text = "Convert", font = ("arial", 18, "bold"), command = convert)
convbutton.place(x = 280, y = 310)

root.mainloop()