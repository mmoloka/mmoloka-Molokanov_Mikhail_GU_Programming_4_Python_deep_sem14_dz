import pytest
from project import*

@pytest.fixture
def project_item():
    return Project()

@pytest.fixture
def project_item_2(project_item):
   project_item.users = project_item.json_reader('log_access.json')
   return project_item

@pytest.fixture
def project_item_3(project_item_2):
   project_item_2.user = project_item_2.enter_system('Тиша', '4')
   return project_item_2

@pytest.fixture
def project_item_4(project_item_2):
   project_item_2.user = project_item_2.enter_system('Вася', '5')
   return project_item_2

def test_json_reader(project_item):
    assert User('5', '1', 'Миша'), User('2', '3', 'Олеся') in project_item.json_reader('log_access.json')

def test_enter_system_success(project_item_2):
   assert project_item_2.enter_system('Олеся', '3') == User('2', '3', 'Олеся')

def test_enter_system_fail(project_item_2):
   with pytest.raises(MyAccessException, match='Пользователь с именем: Гоша и id: 9 отсутствует в базе.'):
      project_item_2.enter_system('Гоша', '9')

def test_add_user_success(project_item_3):
   assert User('2', '7', 'Гоша') in project_item_3.add_user('2', '7', 'Гоша') 

def test_add_user_fail(project_item_4):
   with pytest.raises(MyLevelException, match='Вы не можете добавить пользователя в базу, так как ваш уровень доступа: 1\n\
ниже чем у пользователя: 2'):
         project_item_4.add_user('2', '7', 'Гоша')
                   

if __name__ == '__main__':
 pytest.main()    