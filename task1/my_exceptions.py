# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта. Используйте фикстуры.


class MyException(Exception):
    pass


class MyAccessException(MyException):
    
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f'Пользователь с именем: {self.name} и id: {self.id} отсутствует в базе.'    


class MyLevelException(MyException):
    
    def __init__(self, self_access, other_access):
        self.self_access = self_access
        self.other_access = other_access

    def __str__(self):
        return f'Вы не можете добавить пользователя в базу, так как ваш уровень доступа: {self.self_access}\n\
ниже чем у пользователя: {self.other_access}'