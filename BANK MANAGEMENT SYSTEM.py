class user():
    srno=1
    usercount=0
    def __init__ (self,name,gender):
    
        self.name=name
        self.gender=gender
        
        self.accno=f"121{user.srno}"
        user.srno+=1
        user.usercount+=1
        

    def showdetails(self):
        print(f"name : {self.name}\nGender : {self.gender}\nAccount no : {self.accno}")


class bank(user):
    __balance=0
    def __init__(self,name,gender):
        super().__init__(name,gender)
        
    
    def deposite(self,depamt):
        self.depamt=depamt
        self.__balance+=self.depamt
        print("Transaction successfull!!\n")
        print(f"your current balance is {self.__balance}")
    
    def withdraw(self,widamt):
        self.widamt=widamt
        if self.widamt>self.__balance:
            print(f"Insufficient balance!! your current balance is {self.__balance}")
            print()

        elif self.widamt>=100 and self.widamt<=self.__balance:
            print(f"Transaction successfull!!\n")
            self.__balance-=self.widamt
            print(f"your current balance is {self.__balance}")
            print()

        elif self.widamt<100:
            print(f"you cannot withdraw less than 100 and your current balance is {self.__balance}")
            print()

    def viewbalance(self):
        print(f"your current balance is {self.__balance}")

    
            

    def transfer(self,tamt,user):
        self.tamt=tamt
        if tamt>self.__balance:
            print(f"Insufficient balance!!! your balance is {self.__balance}")
            print()
        elif tamt>=1 and self.tamt<=self.__balance:
            self.__balance=self.__balance-self.tamt
            user.__balance+=tamt
            
            print(f"Amount transfer successfully....your current balance is {self.__balance}")
            print()


print("Welcome to UCO private bank\n")
name=input("Enter your name : ")
print()
gender=input("Enter your gender : ")
print()

o=bank(name,gender)
loop=1
loop1=1
while(loop):
    print("select 1 to check your account details")
    print("select 2 to deposite")
    print("select 3 to withdraw")
    print("select 4 to view balance")
    print("select 5 to transfer")
    print("select 6 to exit\n")

    choice=input("Enter your choice : ")
    print()

    if choice=='1':
        o.showdetails()
        print()

    elif choice=='2':
        depamt=int(input("Enter the amount you want to deposite : "))
        print()
        o.deposite(depamt)
        print()

    elif choice=='3':
        widamt=int(input("Enter the amount you want to withdraw : "))
        print()
        o.withdraw(widamt)
        

    elif choice=='4':
        o.viewbalance()
        print()

    elif choice=='5':
        name1=input("Enter the name of the user you want to transfer : ")
        print()
        gender1=input("Enter the gender of the user you want to transfer : ")
        print()
        b=bank(name1,gender1)
        b.showdetails()
        print()
        tamt=int(input("Enter the amount you want to transfer : "))
        print()
        o.transfer(tamt,b)

    elif choice=='6':
        
        print("Are you sure you want to exit?\n")
        print("If yes enter 'Y' and if no enter 'N'\n")
        while(loop1):
                
            choice1=input("Enter your choice : ").upper()
            print()
            if choice1=='Y':
                loop1-=1
                loop-=1
                print("Thank you for visiting!!!")
    
            elif choice1=='N':
                
                break
            else:
                print("Entered choice in invalid!! please enter again\n")
    else:
        print("Entered choice in invalid!! please enter again\n")
        
                
        
    
            
        
        
        
        
        
        
