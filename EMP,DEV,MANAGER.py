class Employee():
    """This is Parent/ Super class """
    empcount = 0
   # incamt = 1.10 #class attributes
    
    def __init__(self, first, last, salary):
        self.first = first #instance attributes
        self.last = last
        self.salary = salary

        self.email = first.lower()+"."+last.lower()+"@itvedant.com"
        Employee.empcount +=1


    def intro(self):
        return f"{self.first.title()}\n {self.last.title()}\n {self.email} "
    

    def increment(self,incamt):
        self.incamt=incamt
        self.salary = self.salary * self.incamt
        return self.salary


class Developer(Employee):
    def __init__(self, first, last, salary, prolang):
        super().__init__(first, last, salary)
        self.prolang = prolang


class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)

        if(employees is None):
            self.employees = []
        else:
            self.employees = employees
            
    def addemp(self, emp):
        if(emp not in self.employees):
            self.employees.append(emp)
            
    def removeemp(self, emp):
        if(emp in self.employees):
            self.employees.remove(emp)

    def printemp(self):
        for emp in self.employees:
            print(f"---> {emp.fullname()}")



        

emp1 = Employee("raj","yadav", 10000)
emp2 = Employee("deepak","gupta", 20000)
emp3 = Employee("kishor","ramiste", 30000)


mgr1 = Manager('Shubham','Yadav', 40000, [emp1, emp2, emp3])

dev1 = Developer("pratik","singh", 110000, 'Python')
dev2 = Developer("rahul","nishad", 210000, 'Cython')
dev3 = Developer("magesh","thevar", 310000, 'Django')
mgr2 = Manager('Shubham','Yadav', 40000, [dev1, dev2, dev3])

dev4 = Developer("suraj","singh", 110000, 'Python')

while True:
        print("\n")
        print("Enter 1 to Add Employee")
        print("Enter 2 to Add Developer")
        print("Enter 3 to Add Manager")
        print("Enter 4 to Show Employee Details")
        print("Enter 5 to Show Developer Details")
        print("Enter 6 to Show Manager Details")
        print("Enter 7 to Show Increment Employee Salary")
        print("Enter 8 to Show Increment Developer Salary")
        print("Enter 9 to Show Increment Manager Salary")
        print("Enter 10 to Add Employee in Manager")
        print("Enter 11 to Add Developer in Manager")
        print("Enter 12 to Delete Employee from Manager")
        print("Enter 13 to delete Developer from Manager")
        print("Enter 14 to Show Employees and Developer under Manager")
        print("\n")

        choice = input("Enter Your Choice : ").strip()
        print("\n")

        if choice=="1":
            fname=input("enter emp first name: ").strip()
            lname=input("enter emp last name: ").strip()
            sal=float(input("enter sal : "))

            obj1=Employee(fname,lname,sal)

        elif choice=="2":
            fname=input("enter emp first name: ").strip()
            lname=input("enter emp last name: ").strip()
            sal=float(input("enter sal : "))
            prolang=input("enter prog lang: ").strip()

            obj2=Developer(fname,lname,sal,prolang)

        elif choice=="3":
            fname=input("enter emp first name: ").strip()
            lname=input("enter emp last name: ").strip()
            sal=float(input("enter sal : "))

            obj3=Manager(fname,lname,sal)

        elif choice=="4":
            a=obj1.intro()
            print(a)

        elif choice=="5":
            b=obj2.intro()
            print(b)

        elif choice=="6":
            c=obj3.intro()
            print(c)

        elif choice=="7":
            incamt=float(input("enter increment amount: "))
            d=obj1.increment(incamt)
            print(d)

        elif choice=="8":
            incamt=float(input("enter increment amount: "))
            e=obj2.increment(incamt)
            print(e)

        elif choice=="9":
            incamt=float(input("enter increment amount: "))
            f=obj3.increment(incamt)
            print(f)

        elif choice=="10":
            g=obj3.addemp(obj1)
            print(g)

        elif choice=="11":
            h=obj3.addemp(obj2)
            print(h)

        elif choice=="12":
            i=obj3.removeemp(obj1)
            print(i)

        elif choice=="13":
            j=obj3.addemp(obj2)
            print(j)

        elif choice=="14":
            k=obj3.printemp(obj2)
            print(k)

        elif choice=="15":
            break

        
            
            

            


























































































###Employee
##
##class employees():
##    empcount=0
##    incamt=1.15
##    def __init__(self,first,last,salary):
##        self.first=first
##        self.last=last
##        self.salary=salary
##        self.email= f"{self.first.lower()}.{self.last.lower()}.@itvedant.com"
##        employees.empcount+=1
##
##    def intro(Self):
##        print(self.first)
##        print(self.last)
##        print(self.salary)
##        print(self.email)
##
##
##    def increment(self):
##        self.salary=self.salary*self.incamt
##
##    def fullname(self):
##        return f"{self.first.title()} {self.last.title()}"
##
##class developer(employees):
##    incamt= 1.35
##    def __init__(Self,first,last,salary,prolang):
##        super().__init__(first,last,salary)
##        self.prolang=prolang
##
##class manager(employees):
##    def __init__(self,first,last,salary,employees=None):
##        super().__init__(first,last,salary)
##        if(employees is None):
##            self.employees = []
##        else:
##            self.employees= employees
##            
##    def addemp(Self,emp):
##        if(emp in self.employees):
##            self.employees.remove(emp)
##
##    def removeemp(self,emp):
##        if(emp in self.employees):
##            self.employees.remove(emp)
##
##    def printemp(self):
##        for emp in self.employees:
##            print(f"---> {emp.fullname()}")
##        
