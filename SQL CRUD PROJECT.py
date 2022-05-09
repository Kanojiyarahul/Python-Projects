import pymysql as pm
print("imported successfully")

#connecting database
def getconnect():
    return pm.connect(host="localhost",user="root",password="Rahul@123",database="rk")

#showing employees details
def readdata():
    db=getconnect()
    cr=db.cursor()

    sql="select * from employees"
    cr.execute(sql)

    data=cr.fetchall()

    for d in data:
        print(f"{d[0]:^3} {d[1]:^10} {d[2]:^20} {d[3]:^15} {d[4]:^6}\n")

    db.commit()
    db.close()

#inserting data
def insertdata():
    id=input("enter employee Id:").lstrip()
    name=input("enter employee Name:").lstrip()
    
    email=input("enter employee Email:").lstrip()
    mobile=input("enter employee Contact:").lstrip()
    salary=input("enter employee Salary:").lstrip().upper()

    t=(id,name,email,mobile,salary)

    db=getconnect()
    cr=db.cursor()

    sql="insert into employees values(%s,%s,%s,%s,%s);"
    cr.execute(sql, t)

    print("data inserted\n")
    db.commit()
    db.close()

#deleting data
def deletedata():
    id=input("enter employee id here to delete:").lstrip()
    db=getconnect()
    cr=db.cursor()

    sql="delete from employees where id=%s;"
    
    cr.execute(sql, id)
    print("employee details deleted successfully")
    db.commit()
    db.close()

def showdata():
    id=input("enter employee id:").lstrip()
    db=getconnect()
    cr=db.cursor()

    sql="select * from employees where id=%s;"
    cr.execute(sql, id)

    data=cr.fetchall()

    db.commit()
    db.close()
    


    for i in data:
        print(f"{i[0]:^3} {i[1]:^10} {i[2]:^20} {i[3]:^15} {i[4]:^6}\n")

def updatedata(uemp):
    db=getconnect()
    cr=db.cursor()

    if uemp == "1":
        id = input("Enter Employee Id : ").lstrip()
        name = input("Enter New Name : ").lstrip()
        t = (name, id)
        sql = "update employees set name=%s where id = %s;"
        cr.execute(sql,t)

    elif uemp == "2":
        id = input("Enter Employee Id : ").lstrip()
        email = input("Enter New Email : ").lstrip()
        t = (email, id)
        sql = "update employees set email=%s where id = %s;"
        cr.execute(sql,t)

    elif uemp == "3":
        id = input("Enter Employee Id : ").lstrip()
        mobile = input("Enter New mobile no : ").lstrip()
        t = (mobile, id)
        sql = "update employees set mobile=%s where id = %s;"
        cr.execute(sql,t)

    elif uemp == "4":
        id = input("Enter Employee Id : ").lstrip()
        salary = input("Enter New salary : ").lstrip()
        t = (salary, id)
        sql = "update employees set salary=%s where id = %s;"
        cr.execute(sql,t)

    elif uemp == "5":
        id = input("Enter Employee Id : ").lstrip()
        nid = input("Enter New Employee Id : ").lstrip()
        t = (nid, id)
        sql = "update employees set id=%s where id = %s;"
        cr.execute(sql,t)


        print("data updated")
        
    elif uemp=="6":
        uemploop()

    db.commit()
    db.close()

#function for loop

def upemploop():

    while True:
        
        print("\nEnter 1 to Show Emp Full Record")
        print("Enter 2 to Add Employee")
        print("Enter 3 to Update Employee Details")
        print("Enter 4 to Delete Employee Record")
        print("Enter 5 to show Employee Data")
        print("Enter 6 to Exit\n")

        choice = input("Enter your Choice : ").lstrip()
        print("\n")

        if choice == "1":
            readdata()

        elif choice == "2":
            insertdata()

        elif choice == "3":

            print("\nEnter 1 to Update Employee Name")
            print("Enter 2 to Update Employee Email")
            print("Enter 3 to Update Employee Mobile")
            print("Enter 4 to Update Employee Salary")
            print("Enter 5 to Update Employee ID")
            print("Enter 6 to Exit\n")

            uemp=input("Enter Your Choice:").lstrip()
            updatedata(uemp)

        elif choice == "4":
            deletedata()

        elif choice == "5":
            showdata()

        elif choice == "6":
            print("exit")
            break
        else:
            print("Entered choice is invalid!!please choose again.\n")
upemploop()




    
        


    
    

    
    









    

    
