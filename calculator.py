while True:
    print("1. Add values\n2.Subtract values\n3. Multiply values\n4. Divide values\n5.Exit\nEnter your choice number:- ")
    try:
        user_input = int(input())
        if user_input > 5:
            raise Exception
    except:
        print("Please enter number from the given list.")
        continue

    if user_input == 5:
        break

    try:
        a = int(input("Enter 1st number:- "))
        b = int(input("Enter 2nd number:- "))
    except:
        print("Please enter number.")
        continue
    
    if user_input == 1:
        print("Addition of",a,"and",b,"is",a+b)
    if user_input == 2:
        print("Subtraction of",a,"and",b,"is",a-b)
    if user_input == 3:
        print("Multiplication of",a,"and",b,"is",a*b)
    if user_input == 4:
        try:
            print("Division of",a,"and",b,"is {:.3f}".format(a/b))
        except:
            print("Value can't be divided by zero.")
exit()