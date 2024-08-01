#BANK MANAGEMENT SYSTEM



print("_"*80)
print("                                BANK MANAGEMENT SYSTEM")
print("_"*80)

data={}
list1=["Name","Adress","Phone no.","Govt ID","Account Type","Amount"]

def take_data():
    acc_num=input("Enter account number :")
    for item in list1:
        list2.append(input("Enter %s:"%item))

    data[acc_num] = dict(zip(list1,list2))
    print("Account Created")
    print("--"*80)
     
                     
def other_options():
    ch=int(input("1. Check Balance \n2.Withdraw \n3.Deposite \nEnter choice :"))

    if ch==1:
        print("Available balance :",data[acc_num] ["Amount"])
        print("--"*80)

    elif ch==2:
        amt=int(input("Enter amount to withdraw :"))
        new_amt=int(data[acc_num]["Amount"]) -amt
        data[acc_num] ["Amount"] = new_amt
        print("--"*80)
        print("Withdraw successful")
        print("Available Balance :", data[acc_num]["Amount"])
        print("--"*80)

    elif ch==3:
         amt=int(input("Enter amount to deposite :"))
         new_amt=int(data[acc_num] ["Amount"]) +amt
         data[acc_num] ["Amount"]= new_amt
         print("--"*80)
         print("Deposite Successful")
         print("Available Balance :" , data[acc_num] ["Amount"])
         print("--"*80)


while True:
    list2=[]
    ch=int(input("1.New Customer \n2.Existing Customer \n3.Exit \nEnter Choice:"))

    if ch==1:
        take_data()
    if ch==2:
        acc_num = input("Enter Your account number:")
        if acc_num in data:
            print("Record Found!!!")
            other_options()
        else:
            print("Record not found.....")
        if ch==3:
            exit()










    
