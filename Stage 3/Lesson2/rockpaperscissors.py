import random
print("Welcome! Let's play Rock! Paper! Scissors!\n")
print("I am playing....., what will you choose?\n")
global comp
def compInput():    
    x=random.randint(1,10)
    if x<=3:
        comp="Rock"
    elif x>3 and x<=7:
        comp="Paper"
    else:
        comp="Scissors"
    return comp
user=input("\nRock\nPaper\nScissors\n\n")
while(True):
    comp=compInput()
    if(user==comp):
        print("Its a Draw!\n")
    else:
        if user=="Rock":
            if comp=="Paper":
                print("Paper defeats Rock. I Win!\n")
            else:
                print("I picked "+comp+", You win!")

        if user=="Paper":
            if comp=="Rock":
                print("I picked "+comp+"..... "+user+" defeats "+comp+"......You Win!\n")
            else:
                print("I picked "+comp+", I win! ")

        if user=="Scissors":
            if comp=="Rock":
                print("I picked "+comp+"....... "+comp+ " defeats "+ user+"....... I Win! \n")
            else:
                print("I picked "+comp+", You win! ")
    #print("Do you want to continue: Yes/No?")
    #user=input()
    user=input("\nRock\nPaper\nScissors\n\n")
    comp=""
