# Sebastien Lee
# SLee352
# CSC 1301 Proj 1

import calendar
import sys


def main():
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    counter = 1
    days_in_month = calendar.monthrange(year, month)[1]
    day_of_week = 2 + (calendar.monthrange(year, month)[0])

    print("Su Mo Tu We Th Fr Sa")
    print((calendar.month_name[month] + " " + str(year)).center(20))

    for x in range(1, 8):
        if x < day_of_week:
            print('   ', end='')
            counter += 1
    for x in range(1, days_in_month + 1):
        if counter % 7 == 0:
            if x < 10:
                print(' ', end='')
            print(x)
            counter += 1

        else:
            counter += 1
            if x < 10:
                print(' ', end='')
            print(x, '', end='')
    print()

try:
    main()
except Exception as e:
    print(str(e))
