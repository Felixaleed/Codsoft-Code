# Introductory message
print("Welcome to CalcPy!")

while True:
    # Ask user to choose an operation
    print("Choose the operation from the following: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (+, -, *, /): ")
    # Ask user to input their values
    
    num1=float (input("insert num1: "))
    
    num2=float (input("insert num2: "))
    
    # Perform operation
    if operation=="+":
        results= num1+num2 
    
    elif  operation=="-":
        results= num1-num2
    
    elif  operation=="*":
        results= num1*num2
    
    elif  operation=="/":
        if num2!=0:
            results= num1/num2
        else:
            print("Error: cant divide by 0!")
    
    else:
        print("Error: Wrong Operation!")
    
    # Display results
    print("Your Output:", results)
    
    cont = input("Do you want to perform another calculation? (yes/no): ").lower()
    if cont != 'yes':
        break



