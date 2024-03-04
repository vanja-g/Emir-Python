def is_valid_date(date:list):
    if len(date) != 3:
       return False

    day = int(date[0])
    if day > 31 or day < 1:
        return False

    month = int(date[1])
    if month > 12 or month < 1:
        return False

    return True

def is_start_date_bigger_than_end_date(start_date:list,end_date:list):
    start_day, start_month, start_year = start_date
    start_day, start_month, start_year = start_date

    if start_date[2] > end_date[2]:
        return True
    if start_date[1] > end_date[1]:
        return True
    if start_date[0] > end_date[0]:
        return True
    return False
def main():
    date_is_valid = False
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
        if is_start_date_bigger_than_end_date(start_date_elements,end_date_elements):
            print("your start date is bigger than your end date")
            continue

        date_is_valid = True




main()