from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, first_name, last_name, age, password):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
        }

    def __repr__(self):
        return f'User {self.id} {self.first_name} {self.last_name}'
