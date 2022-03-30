from dataclasses import dataclass


@dataclass
class User:
    firstname: str
    lastname: str
    password: str


class Editor:
    def __init__(self):
        self.user_list = []

    def add_user(self, firstname: str, lastname: str, password: str):
        self.user_list.append(User(firstname, lastname, password))

    def view_document(self):
        print('You can see the document!')

    def edit_document(self):
        print('You can not to edit documents in LiteVersion!')


class ProEditor(Editor):
    def edit_document(self):
        print('You can to edit documents in ProVersion!')


def main():
    real_key = 'licensekey1234'
    firstname = input('Enter your firstname: ')
    lastname = input('Enter your lastname: ')
    key = input('Enter the license key: ')

    if key == real_key:
        editor = ProEditor()
    else:
        editor = Editor()

    editor.add_user(firstname, lastname, key)
    print(editor.user_list)
    editor.edit_document()
    editor.view_document()


if __name__ == '__main__':
    main()
