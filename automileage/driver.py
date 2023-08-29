from Date import *


def main():
    print("Please give me a valid date.")
    m = int(input("Enter month (<= 12): "))
    d = int(input("Enter day (<= 31)  : "))
    y = int(input("Enter year (> 0)   : "))
    day = Date(m, d, y)
    print("\nThe date you entered is " + str(day))

    while True:
        menu()
        option = input("Enter your option: ").lower()
        if option == "a":
            n = int(input("Enter number of days to add to the date: "))
            print("\nThe date obtained after adding " + str(n) + \
                  " to " + str(day) + " is " + str(day.add(n)))
        elif option == "t":
            print("\nThe date after " + str(day) + " is " + str(day.tomorrow()))
        elif option == "b":
            print("Please give me another valid date.")
            m2 = int(input("Enter month (<= 12)     : "))
            d2 = int(input("Enter day (<= 31)  : "))
            y2 = int(input("Enter year (> 0)   : "))
            day2 = Date(m2, d2, y2)
            print('day2', day2, type(day2))
            print("\nThe number of days between " + str(day) + " and " + \
                  str(day2) + " is " + str(day.days_between(day2)))
        elif option == "c":
            print("Please give me another valid date.")
            m3 = int(input("Enter month (<= 12): "))
            d3 = int(input("Enter day (<= 31)  : "))
            y3 = int(input("Enter year (> 0)   : "))
            day3 = Date(m3, d3, y3)
            if day.before(day3):
                print("\n" + str(day) + " is before " + str(day3))
            elif day.after(day3):
                print("\n" + str(day) + " is after " + str(day3))
            else:
                print("\n" + str(day) + " is same as " + str(day3))
        elif option == "q":
            break
        else:
            print("Invalid option")


def menu():
    print("\n          Welcome to Date Tester\n")
    print("(a) Add number to the date. ")
    print("(t) Tomorrow. ")
    print("(b) Days between. ")
    print("(c) Compare Dates to see if one is before another. ")
    print("(q) Quit. ")
    print()


main()
