choice = ''
print("Hello! I'm Calculator. What do you want me to do?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
end = False
while(end!=True):

    choice = input("Enter choice(1/2/3/4):")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))


    if choice == '1':
        
        answer = num1+num2
        print(num1,"+",num2,"=", answer)

    elif choice == '2':
        answer = num1-num2
        print(num1,"-",num2,"=", answer)

    elif choice == '3':
        answer = num1*num2
        print(num1,"*",num2,"=", answer)

    elif choice == '4':
        answer = num1/num2
        print(num1,"/",num2,"=", answer)
    else:
        print("Invalid input so exiting")
        end = True