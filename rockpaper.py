
import random
x = int(input("enter a digit i.e. 0 for scissors, 1 for rock and 2 for paper:"))
y = random.randint(0,2)
#procedure
if(x==y):
    print("the computer is"+ str(y)+" you are "+ str(x)+"too. It is a draw")
elif((y==0 and x==1)or(y==1and x==0)or(y==2 and x==0)):
    print("computer wins")
else:
    print("you won")
