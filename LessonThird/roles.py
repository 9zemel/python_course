role = input("Введите вашу роль: ")
age = int(input("Ваш возраст: "))

if role == 'admin' and age > 18:
    print("У вас все права")
elif role == 'user' and age > 16:
    print("У вас есть права пользователя")
else:
    print("этот сервис закрыт на карантин") #актуалочка
    