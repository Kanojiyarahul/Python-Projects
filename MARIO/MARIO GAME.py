class character():
    def __init__(self,name):
        self.name=name
        self.life=3
        self.score=0

    def kicked(self):
        self.score +=10

    def punched(self):
        self.score +=5

    def stabbed(self):
        self.life-=1

    def displaylife(self):
        return self.life

    def displayscore(self):
        return self.score

    def intro(self):
        print(f"name : {self.name}\nlife : {self.life}\nscore : {self.score}\n")

name=input("Enter your name : ")
print()
print(f"welcome to My game {name}")
print()

o=character(name)
loop1 =1
loop2=1

while(loop1):
    print("press 1 to punch")
    print("press 2 to kick")
    print("press 3 to stabb")
    print("press 4 to get scoreboard\n")
    
    choice=input(("enter your choice : "))
    print()

    if choice=='1':
        o.punched()
        print(f"your score is {o.displayscore()}\n")
        
    elif choice=='2':
        o.kicked()
        print(f"your score is {o.displayscore()}\n")

    elif choice=='3':
        o.stabbed()
        print(f"oops!! {o.displaylife()} life left\n")
        
    elif choice=='4':
        o.intro()

    else:
        print(" Entered choice is invalid!!please choose again.\n")
        
    if o.displaylife() ==0:
        print("Game over!!!!\n")
        print(f"your score is {o.displayscore()}")
        print("Do you want to play again?\n")
        print("if yes press 'Y' or if no press 'N'\n")

        while(loop2):
                
            choice1=input("Enter your choice : ").upper()
            print()
        
            if choice1=="Y":
                o.life+=3
                o.score-=o.score
                break
                
                    
            elif choice1=="N":
                print(f"Thank you for playing!!")
                loop2-=1
                loop1-=1
                
            else:
                print("Entered choice is invalid!!please choose again.\n")


        
    

            
                
                

            

            

    
