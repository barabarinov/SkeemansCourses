from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, first_name, last_name, age, password):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'password': self.password,
        }

    def __repr__(self):
        return f'User {self.first_name} {self.last_name}'