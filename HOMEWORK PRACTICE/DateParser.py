
class Date:
    days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, date: str):
        date_parts = date.split(".")
        if len(date_parts) != 3:
            raise ValueError(f"invalid date {date}. must be in format day.month.year")
        self.day = int(date_parts[0])
        self.month = int(date_parts[1])
        self.year = int(date_parts[2])

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
