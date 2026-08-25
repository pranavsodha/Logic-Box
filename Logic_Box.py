print("Welcome To Pattren Generator And Number Analyzer !")


print("Select An Option... \n1. Generate A Pattren \n2. Analyze A Range Of Numbers \n3. Exit")

choice=int(input("Enter Your Choice:"))
if(choice==1):

    rows=int(input("Enter The Number Of Rows In Pattern:"))

    for i in range(1 , rows+1):
        for j in range(i):
            print("*", end="")
        print()
elif(choice==2):

    num1=int(input("Enter The Start Of The Range:"))
    
    num2=int(input("Enter The End Of The Range:"))
    if num1<num2:
        for i in range(num1,num2+1):
            if(i%2==0):
                print(f"Number {i} Is Even.")
            else:
                print(f"Number {i} Is Odd.")
        j=0
        for i in range(num1,num2+1):
            j+=i
        print(f"Sum Of All Numbers From {num1} to {num2} Are: {j}")
    else: 
        print("Invalid Input.......")
    
elif(choice==3):
    
    print("Exiting The Program, Good Bye!")

else:
    print("Invalid Choice..")