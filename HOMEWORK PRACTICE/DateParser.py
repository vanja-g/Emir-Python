
class Date:
    days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __innit__(self, date: str, other, end_date: str):
        date_parts = date.split(".")
        second_date_parts = end_date.split(".")
        if len(date_parts) != 3:
            raise ValueError(f"invalid date {date}. must be in format day.month.year")
        elif len(second_date_parts) != 3:
            raise ValueError(f"invalid date {end_date}. must be in format day.month.year")
        self.day = int(date_parts[0])
        self.month = int(date_parts[1])
        self.year = int(date_parts[2])
        other.day = int(second_date_parts[0])
        other.month = int(second_date_parts[1])
        other.year = int(second_date_parts[2])

    def __gt__(self, other):
        if self.year > other.year:
            return True
        if self.year < other.year:
            return False

        if self.month > other.month:
            return True
        if self.month < other.month:
            return False

        if self.day > other.day:
            return True
        if self.day < other.day:
            return False

    def __lt__(self, other):
        return not(self > other) and (not self == other)

    def __eq__(self, other):
        return ((self.day == other.day)
                 and (self.month == other.month)
                 and (self.year == other.year))



    def isValid(self):
        if self.day > self.days_in_month[self.month] or self.day < 1:
            return False
        if self.month > 12 or self.month < 1:
            return False
        if self.year < 1:
            return False
        return True


    def count_days_between_dates(self, other):
        days_passed = (other.year - self.year) * 365
        if self.month > other.month:
            full_months_passed = 0
            for i in range(self.month - 1, other.month - 1, -1):
                full_months_passed += self.days_in_month[i]
            days_passed -= (full_months_passed + other.day - self.day)

        if self.month < other.month:
            full_months_passed = 0
            for i in range(self.month + 1, other.month + 1):
                full_months_passed += self.days_in_month[i]
            days_passed += (full_months_passed - self.day + other.day)
        else:
            days_passed += self.day - other.day

        return days_passed

    def leap_year(self):
        pass


