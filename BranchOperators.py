if __name__ == '__main__':
    try:
        value = float(input("Enter a value: "))
        choose = input("Enter a choice met or mil: ")

        if choose == "met":
            meters = value * 1609.34
            print("Meters: ", meters)

        elif choose == "mil":
            miles = value / 1609.34
            print("Miles: ", miles)
        else:
            print("Invalid choice")

    except Exception :
        print("Invalid value")

# Path: BranchOperators.py