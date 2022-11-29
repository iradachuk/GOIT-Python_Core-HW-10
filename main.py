from  collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return self.phones

    def remove_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False
    
    def change_phone(self, phone):
        for phone in self.phones:
            if not self.remove_phone(phone):
                self.add_phone(phone)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


address_book = AddressBook()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'No user with given name, try again!'
        except ValueError:
            return 'This user can not be added!'
        except IndexError:
            return 'Unknown command or parameters, please try again!'
    return inner


def greeting(*args):
    return 'How can I help you?'


def good_bye(*args):
    return 'Good bye!'


@input_error
def add_contact(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    record = Record(name.value)
    record.add_phone(phone)
    print(record.add_phone(phone))
    address_book.add_record(record)
    for key, value in address_book.items():
        print(f'{key} - {value}')
    return f'The user with name {name.value} and phone {phone.value} was added!'
    

@input_error
def change_phone(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    record = address_book[name.value]
    record.change_phone(phone)
    return f'The phone number for name {name} was changed!'


@input_error
def show_phone(*args):
    return f'The phone number is: {address_book.get(args[0])}'


def show_all(*args):
    return '\n'.join([f'{name} - {phone}' for name, phone in address_book.items()])


def unknown_command(*args):
    return 'This command is unknown!'


def get_handler(user_input):
    for key, value in COMMANDS.items():
        if user_input.strip().lower().startswith(key):
            command = value
            data = user_input.replace(key, '').split()
    return command, data
    

COMMANDS = {
    'hello': greeting,
    'add': add_contact,
    'change': change_phone,
    'phone': show_phone,
    'show all': show_all,
    'good bye': good_bye,
    'exit': good_bye,
    'close': good_bye
    }


def main():
    while True:
        user_input = input('>>> ')
        if user_input == '.':
            break
        handler, data = get_handler(user_input)
        try:
            result = handler(*data)
            print(result)
        except KeyError:
            print('Unknown command! Try again.')
            main()
        if handler == good_bye:
            break

               
if __name__ == '__main__':
    main()