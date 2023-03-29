if __name__ == "__main__":
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a second number: "))
        num3 = float(input("Enter a third number: "))

        print("What do you want to calculate?")
        print("1. Sum of three numbers")
        print("2. Product of three numbers")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            sum = num1 + num2 + num3
            print("The sum of the three numbers is:", sum)
        elif choice == 2:
            product = num1 * num2 * num3
            print("The product of the three numbers is:", product)
        else:
            print("Invalid choice. Please enter either 1 or 2.")
        pass
    except:
        pass

# Path: BranchOperators.py
