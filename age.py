from datetime import date,datetime
import sys
class Person:
    def __init__(self,birth_date):
        self.birth_date = birth_date
    def calculate_age(self):
        try:
            birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d").date()
            today = date.today()
            age_in_minutes = (today - birth_date).days * 24 * 60
            return age_in_minutes
        except ValueError:
            sys.exit("Invalid date format. Please use YYYY-MM-DD.")
    def validate_birth_date(self):
        try:
            cool_format = datetime.strptime(self.birth_date, "%Y-%m-%d").date()
            if cool_format > date.today():
                sys.exit("Birth date cannot be in the future.")
        except ValueError:
            sys.exit("Invalid date format. Please use YYYY-MM-DD.")

person = Person(input("Enter your birth date (YYYY-MM-DD): "))
person.validate_birth_date()
print(f"Your age in minutes is: {person.calculate_age()}")
