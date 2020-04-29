def titling(name = 'Alena', surname = 'Polyakova'):
    print(name.strip().title()+ " " +surname.strip().title())

user_name = input("Enter user's name: ")
user_surname =input("Enter user's surname: ")
titling(user_name, user_surname) #позиционные аргументы
titling(name=user_name, surname=user_surname) #именованные аргс
# titling() #by default

