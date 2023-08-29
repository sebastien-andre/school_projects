from Date import *
import sys


def header(header_data):
    print('\nAuto Gas Analysis, Year ' + header_data[1] + '\n' + header_data[0] + '\n')
    print('Date' + (16 * ' ') + 'Gallons   $Spent MilesDriven DaysToNextFill    MPG')
    print(70 * '-')


def data_lists(actual_data):
    date_list = []
    gallon_list = []
    spent_list = []
    odometer_list = []
    driven_list = []
    for entry in actual_data:
        date_stop = entry.find(' ')
        date = entry[0:date_stop].split('/')
        month = int(date[0])

        day = int(date[1])
        year = int(date[2])
        date_list.append(Date(month, day, year))

        gallons = float(entry[13:18].strip())
        gallon_list.append(gallons)

        money_spent = float(entry[23:28].strip())
        spent_list.append(money_spent)

        odometer = (int(entry[31:]))
        odometer_list.append(odometer)
    count = 0

    for reading in odometer_list:
        count += 1
        if count == 1:
            continue
        driven_list.append(reading - odometer_list[count - 2])

    return date_list, gallon_list, spent_list, driven_list


def mpg(driven_list, gallon_list):
    mpg_list = []
    for x in enumerate(driven_list):
        if x[0] == len(driven_list):
            continue
        gallon = x[0]
        driven = int(x[1])
        mpg = round(driven / float(gallon_list[gallon]), 2)
        mpg_list.append(mpg)
    return mpg_list


def days_between(date_list):
    days_between_list = []
    for x in enumerate(date_list):
        if (x[0] + 1) == len(date_list):
            continue
        day2_num = x[0] + 1
        day2 = date_list[day2_num]
        day = x[1]
        days_between_list.append(day.days_between(day2))
    return days_between_list


def main():
    with open(str(sys.argv[1]), 'r') as f:
        data = f.read().splitlines()
        f.close()

    header_data = data[:2]
    actual_data = data[2:(len(data) - 1)]
    header(header_data)
    date_list, gallon_list, spent_list, driven_list = data_lists(actual_data)
    mpg_list = mpg(driven_list, gallon_list)
    days_between_list = days_between(date_list)

    gallon_total = str(round((sum(gallon_list)), 2))
    money_spent_total = str(round((sum(spent_list)), 2))
    miles_driven_total = str(round(sum(driven_list)))
    days_between_average = str(round(sum(days_between_list) / len(days_between_list)))
    mpg_average = str(round(sum(mpg_list) / len(mpg_list), 2))

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    formatted_date_list = []
    for item in date_list:
        month_num = int(item._month) - 1
        month = str(months[month_num])
        day = str(item._day)
        year = str(item._year)
        to_print_date = day + ' ' + month + ', ' + year
        formatted_date_list.append(to_print_date)

    for item in enumerate(formatted_date_list):
        x = item[0]
        date = item[1]
        max = len(driven_list)

        gallons = gallon_list[x]
        money_spent = spent_list[x]

        driven = ''
        if x != max:
            driven = driven_list[x]

        between = ''
        if x != max:
            between = days_between_list[x]

        milespg = ''
        if x != max:
            milespg = mpg_list[x]

        print(f"{date:<22}{gallons:>5}{money_spent:>9}"
              f"{driven:>12}{between:>10}{milespg:>12}")

    print(70 * '-')
    print('Totals'f"{gallon_total:>21}{money_spent_total:>9}{miles_driven_total:>12}")
    print('Averages'f"{days_between_average:>50}{mpg_average:>12}")
    print(70 * '-')


main()
