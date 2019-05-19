#import bankproject
import view
import model
import bankproject
def saveusr(d):
    print(d.values())
    C=bankproject.Customer(d['accttype'],d['name'],d['addresscity'],d['addresszipcode'],d['dob'],d['aadhar'],d['pan'],d['username'],d['password'])
    model.insert_df(C)

def login():
        u,p=view.showLogin()
        user= model.login(u,p)
        #print(user)
        if user is not None :
            print("sucessfull login", user)
            if user.get('admin',0) == 1:
                #print('user is a admin')
                d=view.showAdminScreen()
                
                if d[-1] ==1: 
                    saveusr(d[0])
                elif d[-1]==2:
                    model.update(d[0],d[1],d[2])
                elif d[-1]==3: 
                    data=model.searchData(d[0],int(d[1]))
                    print(data)
                    view.displayAccounts(data)
                elif d[-1]==4:
                    s=model.sort1(d[0],d[1])
                    view.displayAccounts(s)
            else:
                print('User is not admin')
                d= view.showTransaction()
                choice=d['choice']
                if choice == 1:
                    model.updatetxn(d['amount'],d['credit'],user.get('accno',0))
                elif choice == 2:
                    view.displayAccounts(model.searchData(d['accno'],d['amount']))
                    view.displayTransactions(model.getTransactions(d['amount']))
                elif choice == 3:
                    d = model.sort2(d['column_name'],d['order'],d['accno'])
                    #print(amt,credit,choice,d)
                    view.displayTransactions(d)
        else:
            print("login not suceesfull")
login()
    
