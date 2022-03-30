# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том,
# что редактирование документов недоступно для бесплатной версии.
# Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.


class Editor:
    def __init__(self, firstname: str, lastname: str, password: str):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.user_list = []

    def add_user(self, firstname: str, lastname: str, password: str):
        self.user_list.append(Editor(firstname, lastname, password))

    def view_document(self):
        print('You can see the document!')

    def edit_document(self):
        print('You can not to edit documents in LiteVersion!')


class ProEditor(Editor):
    def __init__(self):
        super().__init__()

    def edit_document(self):
        print('You can to edit documents in ProVersion!')


def main():
    real_key = 'licensekey1234'
    key = str(input('Enter the license key: '))
    if key == real_key:
        editor = ProEditor()
        firstname = str(input('Enter your firstname: '))
        lastname = str(input('Enter your lastname: '))
        editor.add_user(firstname, lastname, key)
    else:
        editor = Editor()
        firstname = str(input('Enter your firstname: '))
        lastname = str(input('Enter your lastname: '))
        editor.add_user(firstname, lastname, key)

    editor.edit_document()
    editor.view_document()


if __name__ == '__main__':
    main()
