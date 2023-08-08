# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных


def initial_notes():
    with open('phonenumber.txt', 'a', encoding='utf-8') as data: 
        data.write('Иванов Иван Иванович 89234445566')
        data.write('Сидоров Иван Иванович 89235556677')
        data.write('Петров Иван Иванович 89236667788')

def add_note(str):
    surname = input('Введите фамилию:')
    name = input('Введите имя:')
    patronymic = input('Введите отчество:')
    phonenumber = input('Введите номер телефона:')
    str = f'{surname} {name} {patronymic}{phonenumber}\n'
    with open('phonenumber.txt', 'a', encoding='utf-8') as data:
        data.write(str)

def  find_note(str):
    with open('phonenumber.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if str.lower() in line.lower().split():
                print (line, end= '')

def  find_all():
    file = open('phonenumber.txt','r', encoding ='UTF-8')
    data = file.read()
    file.close()
    print (data)
    
   

def delete_note(str):
    lst = []
    with open('phonenumber.txt', 'r', encoding='UTF-8') as data:
        lst = data.readlines()
        for line in range(len(lst)):
           if str.lower( ) in lst[line].lower().split():
              lst[line] = ''
    with open('phonenumber.txt', 'w', encoding='UTF-8') as data:
        for i in lst:
             data.write(i)

def edit_note(str):
    delete_note()
    add_note(str)


#initial_notes()

while True:
    com = input('\n Введите желаемую команду: stop, add, find, all, gen, del, ed: ' )
    if com.lower() == 'stop':
        break
    elif com.lower() == 'add':
        add_note(str)
    elif com.lower() == 'find':
        str = input('Что ищете?')
        find_note(str)
    elif com.lower() == 'all':
        find_all()    
    elif com.lower() == 'del':
        str = input('Что ищете?')
        delete_note(str)
    elif com.lower() == 'ed':
        str = input('Что ищете?')
        edit_note(str)


    



#C:\Users\Павел\Desktop\PythonSem8\phonenumber.txt
