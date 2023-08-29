class Date:
    # Constructor
    def __init__(self, month, day, year):
        self._month = month
        self._day = day
        self._year = year

    def leap_year(self):
        return ((self._year % 4 == 0) and not (self._year % 100 == 0 and self._year % 400 != 0))

    # Returns the Date object one day after self
    def tomorrow(self):
        num_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.leap_year():
            num_days_in_month[1] = 29

        if (self._month == 12) and (self._day == num_days_in_month[11]):
            return Date(1, 1, self._year + 1)
        elif self._day < num_days_in_month[self._month - 1]:
            return Date(self._month, self._day + 1, self._year)
        else:
            return Date(self._month + 1, 1, self._year)

    def yesterday(self):
        num_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.leap_year():
            num_days_in_month[1] = 29

        if (self._month == 1) and (self._day == 1):
            return Date(12, 31, self._year - 1)
        elif self._day == 1:
            return Date(self._month - 1, num_days_in_month[self._month - 2], self._year)
        else:
            return Date(self._month, self._day - 1, self._year)

    # Returns the Date object obtained by adding ndays to self
    def add(self, ndays):
        day = self
        if ndays < 0:
            for x in range(abs(ndays)):
                day = day.yesterday()
            return day
        else:
            for x in range(ndays):
                day = day.tomorrow()
            return day
        # day = Date(self._month, self._day, self._year)

    # Returns True if self is after d
    def after(self, d):
        if self._year > d._year:
            return True
        elif self._year < d._year:
            return False
        elif self._month > d._month:
            return True
        elif self._month < d._month:
            return False
        elif self._day > d._day:
            return True
        else:
            return False

    # Returns True if self is same as d
    def equals(self, d):
        if (self._year == d._year) and (self._month == d._month) and (self._day == d._day):
            return True
        else:
            return False

    # Returns True if self is before d
    def before(self, d):
        if self._year < d._year:
            return True
        elif self._year > d._year:
            return False
        elif self._month < d._month:
            return True
        elif self._month > d._month:
            return False
        elif self._day < d._day:
            return True
        else:
            return False

    # Returns the number of days between self and d
    def days_between(self, d):
        count = 0
        if self.equals(d):
            return 0
        elif self.after(d):
            while True:
                if self.equals(d):
                    break
                count += 1
                d = d.add(1)
        else:
            while True:
                if self.equals(d):
                    break
                d = d.add(-1)
                count += 1
        return count

    def __str__(self):
        return str(self._month) + '/' + str(self._day) + '/' + str(self._year)
