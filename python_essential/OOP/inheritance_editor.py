# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том,
# что редактирование документов недоступно для бесплатной версии.
# Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.


class Editor:
    def __init__(self):
        pass

    def view_document(self):
        pass

    def edit_document(self):
        print('You can not to edit documents in LiteVersion!')


class ProEditor(Editor):

    def edit_document(self):
        print('You can to edit documents in ProVersion!')
