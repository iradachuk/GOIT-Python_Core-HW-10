from  collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value.title()


class Name(Field):
    def __init__(self, *args):
        super().__init__(*args)


class Phone(Field):
    def __init__(self, *args):
        super().__init__(*args)

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(phone)
        return self.phones

    def remove_phone(self, phone):
        self.phones.pop(self.phones.index(phone))
        return self.phones
    
    def change_phone(self, phone, new_phone):
        self.phones.pop(self.phones.index(phone))
        self.phones.append(new_phone)
        return self.phones


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record