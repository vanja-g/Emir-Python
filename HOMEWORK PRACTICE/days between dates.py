days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def count_days_between_dates(start_date: list, end_date: list):
    start_day, start_month, start_year = map(int, start_date)
    end_day, end_month, end_year = map(int, end_date)

    days_passed = (end_year - start_year) * 365
    if start_month > end_month:
        full_months_passed = 0
        for i in range(start_month - 1, end_month - 1, -1):
            full_months_passed += days_in_month[i]
        days_passed -= (full_months_passed + end_day - start_day)

    if start_month < end_month:
        full_months_passed = 0
        for i in range(start_month + 1, end_month + 1):
            full_months_passed += days_in_month[i]
        days_passed += (full_months_passed - start_day + end_day)
    else:
        days_passed += start_day - end_day

    return days_passed

def is_leap_year(year:int):
    pass


def main():
    date_is_valid = False
    start_date = end_date = ""
    start_date_elements = end_date_elements = []

    while not date_is_valid:
        start_date = str(input("what is the first date?"))
        end_date = str(input("what is the second date?"))
        start_date_elements = start_date.split(".")
        end_date_elements = end_date.split(".")

        if not is_valid_date(start_date_elements):
            print("your start date isnt valid")
            continue
        if not is_valid_date(end_date_elements):
            print("your end date isnt valid")
            continue
        if is_start_date_bigger_than_end_date(start_date_elements, end_date_elements):
            print("your start date is bigger than your end date")
            continue

        date_is_valid = True

    days_passed = count_days_between_dates(start_date_elements, end_date_elements)
    print("Days passed between the dates: ", days_passed)


def is_start_date_bigger_than_end_date(start_date: list, end_date: list):
    if start_date[2] > end_date[2]:
        return True
    if start_date[1] > end_date[1]:
        return True
    if start_date[0] > end_date[0]:
        return True
    return False


def is_valid_date(date: list):
    if len(date) != 3:
        return False

    month = int(date[1])
    day = int(date[0])
    if day > days_in_month[month] or day < 1:
        return False

    if month > 12 or month < 1:
        return False

    return True


main()
