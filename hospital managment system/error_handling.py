from datetime import datetime
def get_string(msg):
    while True:
        value = input(msg).strip()
        if all(part.isalpha() for part in value.split()):
            return value
        else:
            print("\nOnly alphabets allowed..... Try again.")

def get_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Please enter only number.")

def get_contact(msg):
    while True:
        value = input(msg)
        if value.isdigit() and len(value) == 10:
            return value
        else:
            print(" Enter valid 10-digit contact number.")

def get_gender(msg):
    while True:
        value = input(msg).lower()
        if value in ['male', 'female', 'other']:
            return value.capitalize()
        else:
            print("please one aff Enter Male / Female / Other.")

def get_date(msg):
    while True:
        value = input(msg)
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Wrong date format. Use YYYY-MM-DD.")
