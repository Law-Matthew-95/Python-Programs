while True:

    def add (x , y):
        return (x + y)

    def minus (x , y):
        return (x - y)

    def times (x , y):
        return (x * y)

    def divide (x , y):
        return (x / y)

    print ("""
    Select an operation;
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """)

    while True:
        choice = int(input("Operation number: "))
        if choice == 1:
            break
        elif choice == 2:
            break
        elif choice == 3:
            break
        elif choice ==4:
            break
        else:
            continue

    while True:
        num1 = int(input("First number: "))
    
        num2 = int(input("Second number: "))

        if choice == 1:
            print(num1 ,"+", num2 ,"=", add(num1 , num2))
        elif choice == 2:
            print(num1 ,"-", num2 ,"=", minus(num1 , num2))
        elif choice == 3:
            print(num1 ,"*", num2 ,"=", times(num1 , num2))
        elif choice == 4:
            print(num1 ,"/", num2 ,"=", divide(num1 , num2))
        else:
            print("Invalid Choices")
        
