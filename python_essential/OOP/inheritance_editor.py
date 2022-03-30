# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том,
# что редактирование документов недоступно для бесплатной версии.
# Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.


class Editor:
    def __init__(self, firststname: str, lastname: str, password: str):
        self.firstname = firststname
        self.lastname = lastname
        self.password = password
        self.user_list = []

    def add_user(self, firstname: str, lastname: str, password: str):
        self.user_list.append(Editor(firstname, lastname, password))

    @staticmethod
    def view_document(self):
        print('You can see the document!')

    def edit_document(self):
        print('You can not to edit documents in LiteVersion!')


class ProEditor(Editor):
    def edit_document(self):
        print('You can to edit documents in ProVersion!')


def main():
    real_key = 'licensekey1234'
    key = str(input('Enter the license key: '))
    if key == real_key:
        firstname = str(input('Enter your firstname: '))
        lastname = str(input('Enter your lastname: '))
        pro_user = ProEditor('User {} {} was created'.format(firstname, lastname))
    else:
        print('Sorry, your key is not valid! But you can register as LiteVersion user!')
        firstname = str(input('Enter your firstname: '))
        lastname = str(input('Enter your lastname: '))
        lite_user = Editor('User {} {} was created'.format(firstname, lastname))


if __name__ == '__main__':
    main()
