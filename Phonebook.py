import time

file = 'Phonebook.txt'

def Menu():
    while True:
        try:
            action = int(input("""
        Введите номер действия:
        1 - Показать все записи
        2 - Найти запись по вхождению частей имени
        3 - Найти запись по вхождению частей фамилии
        4 - Найти запись по телефону
        5 - Добавить новый контакт
        6 - Удалить контакт
        7 - Изменить номер телефона у контакта
        8 - Выход
        ↓↓↓
        """))
            print('')
            
            if action > 0 and action < 9:
                if action == 1: ReadFile(file)
                if action == 2: FindUsersByName(file)
                if action == 3: FindUsersBySurname(file)
                if action == 4: FindPhone(file)
                if action == 5: WriteFile(file)
                if action == 6: DeleteUser(file)
                if action == 7: EditUsers(file)
                if action == 8: break
            else:
                print('Можно выбрать только от 1 до 8 :( Повторите попытку снова')
                time.sleep(2)
                Menu()
            break
        except:
            print('Ошибка! Необходимо ввести номер действия')


def ReadFile(file_name):  # Метод для чтения справочника
    with open(file_name, 'r') as data:
        for line in data:
            string = str(line.strip())
            print(string.replace(",", "", 2))
    print('')
    if int(input("""Вернуться в меню - 1 
""")) == 1:
        Menu()


def FindUsersByName(file_name): # Метод для поиска пользователя по имени или части имени
    name = input("Введите имя для поиска: ")
    print('Результат поиска ↓')
    result = []
    count = 0
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    for user in result:
        if user[1].find(name) == 0:
            print(str(f"Контакт: {user[0]} {user[1]} {user[2]} | Телефон: {user[3]}").replace(",", ""))
            count += 1
    if count == 0:
        print("Данного контака нет в справочнике")
        
    print('')
    choose = int(input("""Вернуться в меню - 1 | Повторить поиск - 2
"""))
    if choose == 1:
        Menu()
    elif choose == 2:
        FindUsersBySurname(file_name)


def FindUsersBySurname(file_name): # Метод для поиска пользователя по имени или части фамилии
    surname = input("Введите фамилию для поиска: ")
    print('Результат поиска ↓')
    result = []
    count = 0
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    for user in result:
        if user[0].find(surname) == 0:
            print(str(f"Контакт: {user[0]} {user[1]} {user[2]} | Телефон: {user[3]}").replace(",", ""))
            count += 1
    if count == 0:
        print("Данного контака нет в справочнике")
    print('')
    choose = int(input("""Вернуться в меню - 1 | Повторить поиск - 2
"""))
    if choose == 1:
        Menu()
    elif choose == 2:
        FindUsersBySurname(file_name) 


def FindPhone(file_name):  # Метод для поиска пользователя по номеру телефона
    phone_number = input("Введите номер телефона поиска: ")
    print('Результат поиска ↓')
    result = []
    count = 0
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    for user in result:
        if user[3].find(phone_number) == 0:
            print(str(f"Контакт: {user[0]} {user[1]} {user[2]} | Телефон: {user[3]}").replace(",", ""))
            count += 1
    if count == 0:
        print("Данного контака нет в справочнике")
    print('')
    choose = int(input("""Вернуться в меню - 1 | Повторить поиск - 2
"""))
    if choose == 1:
        Menu()
    elif choose == 2:
        FindPhone(file_name)   


def WriteFile(file_name):  # Метод для добавления нового польователя
    with open(file_name, 'a+') as data:
        data.writelines('\n')
        data.writelines(input('Фамиля: ') + ",")
        data.writelines(" " + input('Имя: ') + ",")
        data.writelines(" " + input('Отчетство ') + ",")
        data.writelines(" " + input('Телефон: '))
        print('Телефон добавлен в справочник!')
    
    choose = int(input("""Вернуться в меню - 1 | Добавить еще один контакт - 2
"""))
    if choose == 1:
        Menu()
    elif choose == 2:
        WriteFile(file_name) 


def DeleteUser(file_name): # Метод для удаления польователя
    user_surname = input("Введите фамилию контакта для удаления: ")
    import re

    with open(file_name, 'r') as data:
        lines = data.readlines()
    print("") 
    print("Найдены следующие контакты c такой фамилией:")
    result = []
    count = 0
    
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    for user in result:
        if user[0].find(user_surname) == 0:
            print(str(f"{count + 1}. {user[0]} {user[1]} {user[2]} | Телефон: {user[3]}").replace(",", ""))
            count += 1
    if count == 0:
        print("Данного контака нет в справочнике")
        DeleteUser(file_name)        
    else:
        print('Удалить? 1 - Да, 2 - Нет, 3 - Отмена')
        choose = int(input())
        if choose == 2: DeleteUser(file_name)
        if choose == 1:
            user = user_surname
            tamplate = re.compile(re.escape(user))

            with open(file_name, 'w') as data:
                for line in lines:
                    result = tamplate.search(line)
                    if result is None:
                        data.write(line)
                print('Конакт удален')
        if choose == 3:
            Menu()
            exit()
    
    choose2 = int(input("""Вернуться в меню - 1 | Удалить еще один контакт - 2
"""))
    if choose2 == 1:
        Menu()
    elif choose2 == 2:
        DeleteUser(file_name) 
    

def EditUsers(file_name): # Метод для изменения номера телефона у контакта
    user_surname = input("Введите фамилию контакта для изменения номера: ")

    with open(file_name, 'r') as data:
        lines = data.readlines()
    print("") 
    print("Найдены следующие контакты c такой фамилией:")
    result = []
    result_phone = []
    count = 0
    
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    for user in result:
        if user[0].find(user_surname) == 0:
            print(str(f"{count + 1}. {user[0]} {user[1]} {user[2]} | Телефон: {user[3]}").replace(",", ""))
            result_phone = user[3]
            count += 1
    if count == 0:
        print("Данного контака нет в справочнике")
        EditUsers(file_name)        
    else:
        print(f'Изменить номер данного контакта {result_phone} на новый? 1 - Да, 2 - Нет, 3 - Отмена')
        choose = int(input())
        if choose == 2: EditUsers(file_name)
        if choose == 1:
            new_phone_number = input('Введите новый номер телефона: ')
            with open(file_name, 'w') as data:
                for line in lines:
                    result = line.replace(result_phone, new_phone_number)
                    data.write(result)
                print('Номер изменен!')
        if choose == 3: 
            Menu()
            exit()
    
    choose2 = int(input("""Вернуться в меню - 1 | Изменить еще один контакт - 2
"""))
    if choose2 == 1:
        Menu()
    elif choose2 == 2:
        EditUsers(file_name) 

Menu()