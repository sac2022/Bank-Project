import re                                                                              
import sys
from datetime import date 
from datetime import time
from datetime import datetime
class  Person:
	def __init__(self,name,addresscity,addresszipcode,dob,aadhar,pan,username,password):
		self.name=name
		self.addresscity=addresscity
		self.addresszipcode=addresszipcode
		self.dob=dob
		self.aadhar=aadhar
		self.pan=pan
		self.username=username
		self.password=password
	@staticmethod
	def login(username,pwd):
		try:
			f=open("d:\\user.csv")
		except Exception as e:
			print("file not found",e)
			exit()
		rows=f.read().split('\n')
		for row in rows[1:]:	
				print(row)                                                                           
				fields = row.split(',')
				print(fields, username,pwd)
				
				if fields[0] == username.strip() and fields[1] ==pwd.strip() and fields[2] == "1":
					print("admin login successfull ")
					return True
				elif fields[0]== username.strip() and fields[1] ==pwd.strip() and fields[2] == "0":
					print("customer login  successfull")
					return True
	@staticmethod
	def showusernamepwd ():
		print("welcome to bank app")
		try:
			username=input("enter the username:")
			pwd=input("enter the password:")
		except Exception as e:
			print(" user name and password not valid",e)
			
		return (username,pwd)
class Customer:
	def __init__(self,accttype,name,addresscity,addresszipcode,dob,aadhar,pan,username,password,accno=None,balance=0):
		self.accttype=accttype
		self.balance=balance
		self.accno=accno
		self.enable=True
		self.name=name
		self.addresscity=addresscity
		self.addresszipcode=addresszipcode
		self.dob=dob
		self.aadhar=aadhar
		self.pan=pan
		self.username=username
		self.password=password
		#super().__init__(name,addresscity,addresszipcode,dob,aadhar,pan,username,password)
	def enableCustomer(self):
		self.enable= True
	def disableCustomer(self):
		self.enable= False
	def __str__(self):
		return '{} {} {} {} {},{},{}'.format(self.name,self.aadhar,self.accno,self.accttype,self.addresscity,self.addresszipcode,self.dob,self)
	def getFormattedData(self):
		return str(self.accno)+'|'+self.name+'|'+self.addresscity+'|'+str(self.addresszipcode)+'|'+self.dob+'|'+self.aadhar+'|'+self.pan+'|'+str(self.accttype + ',balance=' + str(self.balance) )
	@staticmethod
	def showAdminScreen():
		accounts=readAccounts()
		#print(accounts)
		choice=0
		while choice != 5:
			displayAccounts(accounts)
			print ("1 Register new user")
			print ("2 Enable/Disable account")
			print ("3 Search")
			print ("4 Sort")
			print ("5 Transaction")
			choice = input("Select your choice:")
			choice=int(choice)
			if choice==1:
				Userreg()
			elif choice==2:
				s=input("Enter account no:")
				disableacc(s,accounts)
				saveDisabled(accounts)
			elif choice==3:
				s=input("Enter account no:")
				searchaccounts(s,accounts)
			elif choice==4:
				s=int(input("Enter sort column (1.id,2.name,3.account type:"))
				if s == 1:
					sort(accounts,{'id':'asc'})
				if s == 2:
					sort(accounts,{'name':'asc'})
				if s == 3:
					sort(accounts,{'type':'asc'})
			elif choice==5:
					#trans=readTransactions()
					Transaction.showTransaction()
					#check
		return 0
class admin(Person):
	def __init__(self):
		username,pwd = Person.showusernamepwd()
		print(username,pwd)
		if Person.login(username,pwd):
			Customer.showAdminScreen()
def searchaccounts(accno,accounts):
		results=[]
		for acc in accounts:
			#print(acc.accno,accno)
			if acc.accno == accno:
				results+=[acc]
				print(acc.getFormattedData())
		print("search is completed")
def displayAccounts(accounts):
		for row in accounts[1:]:
			if row.enable:
				print(row.getFormattedData())
def disableacc(accno,accounts):
		for row in accounts[1:]:
			if row.accno==accno:
				row.disable()
				print("account is disabled",accno)
				break
def sort(accounts,d={'id':'asc'}):
	#print(accounts)
	#for result in accounts:
	#	print(result.getFormattedData())
	results=[]
	if 'id' in d.keys() and d['id'] == 'asc':
		results=sorted(accounts,key=lambda x:x.accno)
	if 'id' in d.keys() and d['id'] == 'dsc':
		results=sorted(accounts,key=lambda x:x.accno,reverse=True)
	if 'name' in d.keys() and d['name'] == 'asc':
		results=sorted(accounts,key=lambda x:x.name)
	if 'name' in d.keys() and d['name'] == 'dsc':
		results=sorted(accounts,key=lambda x:x.name,reverse=True)
	if 'type' in d.keys() and d['type'] == 'asc':
		results=sorted(accounts,key=lambda x:x.accttype)
	if 'type' in d.keys() and d['type'] == 'dsc':
		results=sorted(accounts,key=lambda x:x.accttype,reverse=True)
	#print(results)
	for result in results:
		print(result.getFormattedData())
		break
def readbalance(amt):
	accounts=readAccounts()
	trans=readTransactions()
	if Customer.accno==Transaction.accno:
		if Customer.balance>amt:
			print("no balance")
			exit()
	return accounts.balance

	
def readTransactions():
	try:
		f=open("d:\\trans.csv")
	except Exception as e:
		print("no file found",e)
	rows=f.read().split('\n')
	header=rows[0].split(',')
	transactions=[]
	for row in rows[1:]:
		row=row.split(',')
		print(row)
		t1=Transaction(row[0],row[1],row[2],row[3],row[4])
		transactions.append(t1)
	return transactions
def transgen():
	f=open("d:\\trans.csv")
	lastRow = f.read().split(',')
	nexttrans=1
	if (lastRow[0].isnumeric()):		
		nexttrans = int(lastRow[0])+1
	#str(nexttrans)
	#f.write(nexttrans)
	f.close()
	return nexttrans
def displayTransaction(transaction):
		for row in transaction[1:]:
			print(row.getformatdata())
class Transaction(Person):
	def __init__(self,transid,accno,amt,credit,datime):
		self.transid=transid
		self.accno=accno
		self.datime=datime
		self.credit=credit
		self.creditDisplay='Withdraw'
		if credit:
			self.creditDisplay = 'Credit'
		self.amt=amt
		#print(transid,accno,datime,amt)
	def getformatdata(self):
		return	self.creditDisplay + ',' +str(self.transid)+str(self.accno)+','+str(self.amt)+','+str(self.datime)
	@staticmethod
	def inpwith():
		amt=input("enter the amt to be withdrawn")
		return amt
	@staticmethod
	def inpdep():
		credit=input("enter the amt to be deposite")
		return credit
	@staticmethod
	def writedata(self,data,credit=True):
		try:
			f=open("d:\\trans.csv","w")
			o=open("d:\\trans.csv")
		except Exception as e:
			print("no file found",e)
		rows=o.read().split('\n')
		header=rows[0].split(',')
		for row in rows[1:]:
			row=row.split(',')
			s=int(transgen())+","+str(self.accno)+","+self.amt+","+str(data)+","+str(datetime.now())
			print(s)
			f.write(s)
		f.close() 
	@staticmethod
	def withdrawndeposite():
		choice=0
		choice=int(input("enter the choice 1:withdraw 2:deposite 3 exit:"))
		while choice !=3:
			if choice>3:
				print("invalid option re-enter the option")
				continue
			if choice==1:
				amt=int(input("Enter amount to withdraw:"))
				return amt,False,1
			elif choice==2:
				amt=int(input("Enter amount to deploisted:"))
				return amt,True,1
			elif choice==3:
				exit()
	def searchTrans(transid,transaction):
		results=[]
		for tr in transaction:
			#print(acc.accno,accno)
			if tr.transid == transid:
				results+=[tr]
				print(tr.getformatdata())
		print("search is completed")
	@staticmethod
	def showTransaction():
		#transaction=readTransactions()
		#print(transaction)
		choice=0
		while choice != 5:
			#displayTransaction(transaction)
			print ("1 deposite n withdraw")
			print ("2 search")
			print ("3 sort")
			print ("4 exit")
			choice = input("Select your choice:")
			choice=int(choice)
			if choice>5:
				print("invalid option")
				continue
			if choice==1:
				Transaction.withdrawndeposite()
				datasave(transaction)
			elif choice==2:
				transid=input("enter the transid")
				Transaction.searchTrans(transid,transaction)
			elif choice==3:
					pass
			elif choice==4:
					exit()
			
				
		return 0
def readAccounts():
		try:
			f=open("D:\\usrdata.dat")
		except Exception as e:
			print("no file found",e)
		rows=f.read().split('\n')
		header=rows[0].split(',')
		accounts=[]
		for row in rows[1:]:
			row=row.split(',')
			#accttype,balance,accno,name,addr,dob,aadhar,pan,username,password
			t= Customer(row[6],row[7],row[0],row[1],row[2],row[3],row[4],row[5],'','')
			accounts.append(t)
		return accounts
def datasave(transaction):
		try:
			s=''
			 
			for t in transaction:
				s+='\n'+t.getformatdata()
			f=open("trans.csv","w")
			f.write(s)
			f.close()
		except Exception as e:
			print("",e)
def savedata(cust):
		try:
			f=open("d:\\usrdata.dat","a")
			f.write('\n'+cust.getFormattedData())
			f.close()
		except Exception as e:
			print("filenotfound",e)
def saveDisabled(accounts):
		try:
			s='accno,name,addr,dob,aadhar,pan,accttype,bal,enable'
			for  a in accounts:
				s+='\n'+a.getFormattedData()
			f=open("d:\\usrdata.dat","w")
			f.write(s)
		except Exception as e:
			print("filenotfound",e)
			f.close()
def savelogindata(cust):
		try:
			f=open("d:\\user.csv","a")
			f.write('\n'+cust.username+','+cust.password+',0')
			f.close()
		except Exception as e:
			print("filenotfound",e)
def Userreg():
		print("user registration\n")
		name=input("enter the name")
		dob=input("enter the dob")
		addr=input("enter the addr")
		pan=input("enter the pan")
		aadhar=input("enter the aadhar num")
		saving=input("saving or current \n s for saving and for c current")
		username=input("enter username")
		password=input("enter password")
		
		if re.findall('[A-Z][0-9][A-Z]*',pan):
				print("pan is in correct format",pan)
		else:
				print("pan is invalid format ,renter the pan number",pan)
				pan=input("enter the pan")
		if re.findall('[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]',aadhar):
			print("validate format",aadhar)
		else:
				print("renter the number in correct format")
				aadhar=input("enter the aadhar num")
		if re.findall('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]',dob):
			print("date",dob)
                        
		else:
				print("reenter the dob")
				dob=input("enter the dob")
		cust = Customer(saving,0,getAccNo(),name,addr,dob,aadhar,pan,username,password)
		savedata(cust)		
		savelogindata(cust)		
def getAccNo():
	f=open('d:\\usrdata.dat')
	lastRow = f.read().split('\n')[-1]
	nextAcctNo=1
	if (lastRow[0].isnumeric()):		
		nextAcctNo = int(lastRow[0])+1
	f.close()
	return nextAcctNo

#p1=Custontmer('saving','100','1022','sachin','270491','10990aa','apgp12','yes','sachin','pwd')
#print(p1)
#a=admin()
#t=Transaction('transid','accno','amt','credit','datime')
#t.showTransaction()
