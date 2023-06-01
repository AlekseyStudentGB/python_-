


# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать тк
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход


def open_ts():
    if control == False:
        with open('text.txt', 'r') as data:
            temp_list = [line for line in data]
            for values in temp_list:
                values = values.strip().split(';')
                contacts.append({'name' : values[0], 'phone' : values[1]}) 
            
            print('*телефонный справочник открыт*\n')
    else:
        print('*!!! телефонный справочник уже был открыт ранее !!!*')

def show_ts():
    if control == False:
        print('*для начала откройте ТС используя команду "1"*')
    else:
        if len(contacts) < 1:
            print('*Телефонный справочник пуст*')   
        else :
            print()
            i = 1
            for contact in contacts:
                string = ''.join(item + ' ' for item in contact.values())
                print(f'{i} {string}')
                i += 1
            
def add_contact():
    
    contacts.append({'name':input('\nВведите имя -> '),'phone':input('Введите номер -> ')})  if  control != False else print('*для начала откройте ТС используя команду "1"*')
    
    
def work_string():
    string = ''
    for contact in contacts:
        string += ';'.join([value for value in contact.values()]) + '\n'
    
        
    return string[:-1]

def seve_ts(): 
    if control == False:
        print('*для начала откройте ТС используя команду "1"*')
    else:
        with open('text.txt', 'w') as data:
            data.write(work_string())
            print('*Контакт сохранен*')                

def get_contact():
    seek = input('\nВедите имя для поиска ->').lower()
    print('Результат поиска:', end='\n')
    index = 1
    for contact in contacts:
        if seek in contact['name'].lower():
            n,p = contact['name'],contact['phone']
            print(f'{index}. {n} {p}' )
        index += 1
         

def change_contact():
    show_ts()
    chenge_number = int(input('Введите номер контакта который вы хотите изменить'))
    name = input('Введите новое имя выбранного контакта или нажмите "Entr" чтобы оставить его прежним -> ')
    phone = input('Введите новый телефонный номер выбранного контакта или нажмите "Entr" чтобы оставить его прежним -> ')
 
    contacts[chenge_number-1]['name'] = name  if len(name) > 0 else contacts[chenge_number-1]['name']
    phone = contacts[chenge_number-1]['phone']= phone if len(phone) > 0 else contacts[chenge_number-1]['phone']
    
def delet_contacts():
    show_ts()
    contacts.pop(int(input('Введите номер контакта который вы хотите изменить'))-1)
    print('Введите номер контакта который вы хотите изменить')

menu = '''__________________
   MENU:
1. Открыть файл
2. Сохранить файл
3. Показать тк
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход
////////////////////'''
contacts = []
comand = 0
control = False
while comand != 8:
    print(menu)
    comand = int(input('введите команду -> '))
    print('''выполнения команды : ''', end=' ')
    

    if comand == 1:
        open_ts()
        control = True
    elif comand == 2:
        seve_ts()
    elif comand == 3:
        show_ts()   
    elif comand == 4:
        add_contact()
    elif comand == 5:
        get_contact()
    elif comand == 6:
        change_contact()
    elif comand == 7:
        delet_contacts()
    elif comand == 8:
        print('*программа закрыта*')
print('\nВсегО хОрОшегО!!!')