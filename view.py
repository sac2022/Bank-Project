from Crypto import Random
import base64
import re
from datetime import date 
from datetime import time
from datetime import datetime
import sys
#import model
from bankproject import Transaction
from bankproject import Customer
#from bankproject import Person
import base64
def showLogin():
		username=input("enter the user name:\t")
		password=input("enter the password:\t")
		p=base64.b64encode(bytes(password,'utf-8'))
		return username,p.decode()
def showAdminScreen():

	choice=0
	while choice != 5:
		print ("1 Register new user")
		print ("2 Enable/Disable account")
		print ("3 Search")
		print ("4 Sort")
		print ("5 Transaction")
		choice=input("Select your choice:")
		choice=int(choice)
		if choice==1:
			return insert_de(),choice
		elif choice==2:
			s=input("Enter account no:")			
			enable=input("E for Enable/D for Disable:")
			return s,'enable',enable,choice

		elif choice==3:
			s=input("Enter account no:")
			return 'accno',s,choice
		elif choice==4:
			s=input("Enter sort column id,name,accno:")
			order=int(input("Enter sort order 1 for asc or -1 for desc"))
			return s,order,choice
		elif choice==5:
			exit()
def displayAccounts(d):
	for data in d:
		displayAccount(data)
def displayAccount(d):
	print(d.getFormattedData())	
def displayTransactions(d):
	#print(d)
	for doc in d:
		print(doc.getformatdata())	

def withdrawndeposite():
		choice=0
		choice=int(input("enter the choice 1:withdraw 2:deposite 3 exit:"))
		while choice !=3:
			if choice>3:
				print("invalid option re-enter the option")
				continue
			if choice==1:
				amt=int(input("Enter amount to withdraw:"))
                                #r=readbalance(amt)
                                #tr=Transaction.writedata(amt,True)
			elif choice==2:
				amt=int(input("Enter amount to deploisted:"))
                                #tr=Transaction.writedata(amt,True)
			elif choice==3:
                                exit()

def showTransaction():
		choice=0
		while choice != 5:
			print ("1 deposite n withdraw")
			print ("2 search")
			print ("3 sort")
			print ("4 exit")
			choice = input("Select your choice:")
			choice=int(choice)
			if choice>=5:
				print("invalid option")
				continue
			if choice==1:
				dw=input('Deposit(D) or Wihtdraw(W)')
				amt=input("Enter amount:")
				credit=True
				if dw=='W': credit=False
				return {'amt':amt,'credit':credit,'choice':choice}
			elif choice==2:
				transid=int(input("enter the transid"))
				return {'transid':transid,'choice':choice}
			elif choice==3:
				s=input("Enter accno :")
				t = input ("Enter sort column - dt, id, amount:")
				order=int(input("Enter sort order 1 for asc or -1 for desc"))
				return {'accno':s,'column_name':t,'order':order,'choice':choice}
			elif choice==4:
				exit()
def insert_de():
		name=input("enter the name:")
		dob=input("enter dob:")
		pan=str(input("enter the PAN number:"))
		aadhar=str(input("enter the aadhar number:"))
		addresscity=str(input("enter the city:"))
		addresszipcode=int(input("enter the zip code:"))
		username=input("enter the user name")
		password=input("enter the password")
		accttype=input("enter the account type")
		
		p=base64.b64encode(password.encode())
		return {'name':name,'dob':dob,'pan':pan,'aadhar':aadhar,
				'addresscity':addresscity,
				'addresszipcode':addresszipcode,
				'username':username,'password':p.decode(),'accttype':accttype}
#import model1
#print(model.ser_de('accno','2'))
#showAdminScreen()
