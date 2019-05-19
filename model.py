#!/usr/bin/env python
import sys
import string
import random
import pymongo
import datetime
from pymongo import MongoClient
import view
from bankproject import Customer, Transaction

client=MongoClient("localhost",27017)
db=client.bank
def updatetxn(amount,credit,accno):
	for cur in db.person.find({'accno':accno},{'balance':1}):
		bal = cur.get('balance',0)
		if credit==False and amount > bal:
			print("You do not have sufficient balance ")
			return
		else:
			break
	db.person.update_one({"accno":accno},{"$push":{"transactions":{"id":generateTxNo(accno),"amount":amount,"credit":credit,"dt":datetime.datetime.now()}}})
	if credit:
		db.person.update_one({'accno':accno},{"$inc":{'balance':amount}})
	else :
		amount *=-1
		db.person.update_one({'accno':accno},{"$inc":{'balance':amount}})

def up():
	cust=db.person.find()
	for c in cust:
		rows=random.randint(1,10)
		for i in range(rows):
			credit=[True,False]
			id=random.randint(1,9999)
			amount=random.randint(1,10)*1000
			credit=random.randint(0,1)
			str(c["_id"])
	updatetxn(id,amount,credit,generatedatetime(),c["_id"])
	print(id,amount,credit,generatedatetime(),c["_id"])
def insert_df(c):
	#name,pan,aadhar,addresscity,addressstreet,addresszipcode= view.insert_de()
	try:
		#print(c)
		_id=db.person.insert_one({'accno':generateAcctNo(),"name":c.name,"pan":c.pan,"aadhar":c.aadhar,"addresscity":c.addresscity,"addresszipcode":c.addresszipcode,'username':c.username, 'password':c.password,'dob':c.dob})
		print(_id.inserted_id)
		return _id.inserted_id
	except Exception as e:
		print(e)
	return 
def del_de(k,v):
	try:
		db.person.delete_one({k:v});
	except Exception as e:
		print(e)
def searchData(k,v):
    #try:
    data=[]
    print(k,v)
    for d in db.person.find({k:v}):
        #print(d)
        #exit(0)
        data+=[Customer(d.get('accttype','Savings'),d.get('name',None),d.get('addresscity',None),d.get('addresszipcode',None),d.get('dob',None),d.get('aadhar',None),d.get('pan',None),d.get('username',None),d.get('password',''),d.get('accno',0),d.get('balance',0))]
        #print(data[0])
    return data
    #except Exception as e:
    #	print(e)
#print(ser_de("name","Adrienn"))
def update(accno,k,v):
	db.person.update_one({"accno":int(accno)},{"$set":{k:v}})
def login(username,password):
	 #usrname,password=view.showLogin()

	 for c in db.person.find({'username':username,'password':str(password)}):
		 return c
def generateAcctNo():	
	x=db.person.find({},{'accno':1}).sort([('accno',-1)]).limit(1)
	for k in x:
		return k.get('accno',1)+1
	return 1
def generateTxNo(accno):	
	for x in db.person.find({'accno':accno},{'transactions':1}):
		if 'transactions' not in x.keys():
			return 1
		txns = x['transactions']
		if txns is not None:
			y=[t['id'] for t in txns]
			return max(y)+1
	return 1
def getTransactions(accno):	
	for x in db.person.find({'accno':accno},{'transactions':1}):
		txns = x['transactions']
		if txns is not None:
			y=[Transaction(t['id'],accno,t['amount'],t['credit'],t['dt']) for t in txns]
			return y
	return None

def sort1(name,asc):
    x=db.person.find({'username':{'$ne':'admin'}}).sort([(name,asc)])
    data=[]
    for d in x:
        data+=[Customer(d.get('accttype','Savings'),d.get('name',None),d.get('addresscity',None),d.get('addresszipcode',None),d.get('dob',None),d.get('aadhar',None),d.get('pan',None),d.get('username',None),d.get('password',''),d.get('accno',0),0)]
    return data
def sort2(columnName,order,accno):
	#print(n,asc,accno)
	from bson.son import SON
	pipeline=[
			{'$match':{'accno':accno}},
			{'$unwind':'$transactions'},
			{'$sort':SON( [ ('transactions.'+columnName,order) ] ) }
	]
	#x=db.person.find({'accno':accno}).sort([(n,asc)])

	x=list(db.person.aggregate(pipeline))
	data=[]
	for d in x:
		t=d.get('transactions')
		#print(t.get('dt'))
		data+=[Transaction(t.get('id'),t.get('accno'),t.get('amount'),t.get('credit'),t.get('dt'))]
	return data


	
#print(generateAcctNo())
#import base64
#p=base64.b64encode(bytes('admin','utf-8'))
#print(p,p.decode())
#print(login('admin',p.decode()))

#c=Customer('saving','100','12','Ram','bangalore','karnataka','27-04-91','123-560-55','APGP583','admin','admin')
#print(c)
#insert_df(c)
#print(searchData('accno',2))
#update(2,'enable','e')

#print(generateTxNo(3))
#print(sort2('dt',-1,3))