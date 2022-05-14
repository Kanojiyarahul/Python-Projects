import os as o


def mkdir(folder):
    i=o.mkdir(folder)
    return i

def rmdir(folder1):
    j=o.rmdir(folder1)
    return j

def remove(folder2):
    k=o.remove(folder2)
    return k

def fdirct():
    l=o.getcwd()
    return l




a=1
b=1

while a:
    print(f"select1: show files and folders in desktop\n")
    print(f"select2: create folders in desktop\n")
    print(f"select3: remove folders from desktop\n")
    print(f"select4: remove files from desktop\n")
    print(f"select5: Current working Directory\n")
    print(f"select6: To Exit\n")
    

    choice=input("enter your choice: ")
    print()

    if choice=="1":
        print(o.listdir())
        
    
    elif choice=="2":
        folder=input("enter folder name to create: ")
        o.mkdir(folder)
        print("folder created successfully...!\n\n")

    elif choice=="3":
        folder1=input("enter folder name to delete: ")
        o.rmdir(folder1)
        print("folder deleted successfully...!\n\n")

    elif choice=="4":
        folder2=input("enter file name to delete: ")
        o.remove(folder2)
        print("file deleted successfully...!\n\n")


    elif choice=="5":
        folder3=o.getcwd()
        print(folder3)

    elif choice=="6":
        
        
        print("Are you sure you want to exit..!\n")
        print("if yes enter Y & for no enter N\n")
        
        while b:
            choice2=input("enter your choice: ").upper()

            if choice2=="Y":
                a=a-1                                        
                break
                
            elif choice2=="N":
                
                break

            else:
                print("invalid choice please enter valid choice here:.. \n")


    else:
        print("invalid choice please enter valid choice here:..")
        print()
    
            
    
    
