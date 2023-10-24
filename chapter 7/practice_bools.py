"""Starts with any number of letters, numbers and a dot"""
"""Has an @"""
"""The @ is followed by a valid domain (google or yahoo, microsoft)"""
"""google and yahoo domains end with .com, but microsoft ends with .mail"""

def main():
    user_email = str(input("enter an email address to be validated "))
    valid_characters = "abcdefghijklmnopqrstucwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.0123456789"

    is_valid = True
    if "@" in user_email:
        first_part = user_email[0: user_email.find("@")]
        for char in first_part:
            if char not in valid_characters:
                is_valid = False

        if not(is_google_or_yahoo(user_email) or is_microsoft(user_email)):
            is_valid = False
    else:
        is_valid = False



    if is_valid:
        print("Valid")
    else:
        print("Invalid")


def is_google_or_yahoo(user_email):
    return user_email.endswith(".com") and user_email[user_email.find("@") + 1 : user_email.find(".com")] in ["gmail", "yahoo"]

def is_microsoft(user_email):
    return user_email.endswith(".mail") and user_email[user_email.find("@") + 1 : user_email.find(".mail")] == "microsoft"





main()