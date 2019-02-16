#Read an integer:
print('Enter a Ladder Size to Build:')
a = int(input())
#Building a ladder:

print() # This is for a new line

for i in range(0,a): # Outer Loop to Run the program for 6 Ladder Steps
    for j in range (0,i+1): #Inner Loop to Print the Number for Each Step
        print(".",end="")
    print()
