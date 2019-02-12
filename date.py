import time

class Date:
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

    def string_to_model(self, date_str):
        date = date_str.split('.')
        self.day = int(date[0])
        self.month = int(date[1])
        self.year = int(date[2])

    def get_duration(self, date_to):
        feb = 28
        if Date.is_leap_year(self.year):
            feb = 29
        month_lengths = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == date_to.month:
            return date_to.day - self.day
        else:
            return month_lengths[self.month - 1] - self.day + date_to.day

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0 and year % 100 != 0 :
            return True
        else:
            return year % 4 == 0 and year % 100 == 0 and year % 400 == 0

    @staticmethod
    def get_current():
        return time.strftime("%d.%m.%Y")


d = Date()
d.string_to_model("16.07.2002")