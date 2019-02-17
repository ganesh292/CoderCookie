#Read an integer:
print('Enter number to build a multiplication table:')
a = int(input())
#Building a ladder:

print() # This is for a new line

###Nested Loops
#for i in range(1,a+1): # Outer Loop to Run the program for 6 Ladder Steps
#    for j in range (1,11): #Inner Loop to Print the Number for Each Step
 #       print(str(i)+" X "+str(j)+" = "+str(i*j))
#    print()

###Single loop
for j in range(1,11):
    print(str(a)+" X "+str(j)+" = "+str(a*j))

###Using While loop
#j=1
#while j!=11:
#    print(str(a)+" X "+str(j)+" = "+str(a*j))
#    j=j+1
