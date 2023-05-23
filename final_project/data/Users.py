from dataclasses import dataclass


@dataclass
class User:
    first_name = str
    last_name = str
    email = str
    gender = str
    phone_number = str
    hobby = str
    day = int
    month = int
    year = int

    key_letters = str
    subject = str
    file_name = str
    address = str
    state = str
    city = str

    def __init__(self, first_name, last_name, email, gender, phone_number, hobby, day,
                 month, year, key_letters, subject, file_name, address, state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.phone_number = phone_number
        self.hobby = hobby
        self.day = day
        self.month = month
        self.year = year

        self.key_letters = key_letters
        self.subject = subject
        self.file_name = file_name
        self.address = address
        self.state = state
        self.city = city
