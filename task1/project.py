import json
from my_exceptions import MyAccessException, MyLevelException


class User:

    def __init__(self, access: int, id: int, name: str):
        self.access = access
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.access} - {self.id} - {self.name}'
    
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
    
    def __hash__(self):
        return hash((self.name, self.id))


class Project:

    def __init__(self):
        self.user = None
        self.users = set()

    def json_reader(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
        for access, value in my_dict.items():
            for id, name in value.items():
                self.users.add(User(access, id, name))
        return self.users
    
    def enter_system(self, name, id):
        user = User(0, id, name)
        if user not in self.users:
            raise MyAccessException(name, id)
        for temp in self.users:
            if temp == user:
                self.user = temp
        return self.user
    
    def add_user(self, access, id, name):
        if self.user.access < access:
            raise MyLevelException(self.user.access, access)
        else:
            user = User(access, id, name)
            self.users.add(user)
        return self.users