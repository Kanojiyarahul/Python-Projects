def read(r):
    file=open(r,"r")
    cont=file.read()
    file.close()
    print(cont)
def write(w,insert):
    file=open(w,"w")
    
    file.write(insert)
    file.close

def append(a,insert):
    file=open(a,"a")
    file.write(insert)
    file.close()



loop1=1
loop2=1

while(loop1):
    
    print("select 1 to open and Read a file")
    print("select 2 to open and write in a file")
    print("select 3 to open and append in a file")
    print("select 4 to exit\n")

    choice=input("Enter your choice : ").strip()
    print()

    if choice=='1':
        r=input("Enter file name with extension : ").strip()
        read(r)
        print()
        


    elif choice=='2':
        w=input("Enter file name with extension : ").strip()
        print()
        insert=input("Enter here what u want to write : ")
        write(w,insert)
        print()

    elif choice=='3':
        a=input("Enter file name with extension : ").strip()
        print()
        insert=input("Enter here what u want append  in a file : ")
        append(a,insert)
        print()

    elif choice=='4':
        break

    else:
        print("Entered choice is invalid!!!please enter your choice again.\n")

    
    
