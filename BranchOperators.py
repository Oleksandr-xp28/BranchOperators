if __name__ == "__main__":
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        num3 = int(input("Enter a third number: "))

        # initialize variables for max and min
        max_num = num1
        min_num = num1
        # list
        for num in [num1, num2, num3]:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num

        choice = input("Enter 'max' or 'min': ")

        if choice == 'max':
            print("The maximum number is", max_num)
        elif choice == 'min':
            print("The minimum number is", min_num)
        else:
            print("Invalid choice. Please enter 'max' or 'min'.")

#       if choice == 1:
#           print("Max number is: ", max(num1, num2, num3))
#       elif choice == 2:
#            print("Min number is: ", min(num1, num2, num3))
#       else:
#            print("Invalid choice.")
    except:
        print("Invalid choice.") 

        
