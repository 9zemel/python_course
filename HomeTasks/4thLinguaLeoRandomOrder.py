slovar = {"goose": "гусь", "moose": "лось", "salmon": "лосось", "whale": "кит"}

print("Добро пожаловать в LinguaLeo Light Edition!\n")

answer = 0
while answer != 3:
    print(
    '''
    Выберите пункт меню:
    1 - добавить новые слова в словарь
    2 - тренировка
    3 - выход
    '''
    )
    answer = int(input("Ваш выбор: "))
    if answer == 1:
        print("Для выхода в меню введите 'stop'\n")
        while True:
            key = input('Введите слово на английском: ').strip().lower()
            if key == 'stop':
                break
            value = input('Введите перевод: ').strip().lower()
            slovar[key] = value
    elif answer == 2:
        print("Сейчас начнется тренировка. Вы можете допустить не более 3ех ошибок\n")
        print(slovar)
        errors = 0
        bonus = 0
        keys_list = set(slovar.keys()) #я использовала сет, потому что мы его проходили, для закрепления материала
                                    #также работает через keys_list = list(slovar.keys()) random.shuffle(keys_list)
        for key in keys_list:
            print("Введите перевод для слова", key,":")
            answer = input(":").strip().lower()
            if slovar[key] == answer:
                bonus += 1
                print("Бонусные очки: ",bonus)
            elif errors > 3:
                print("Вы превысили лимит ошибок, тренировка окончена ")
                break
            else:
                errors += 1
                print("Ошибка! Правильный перевод для",key,"- это",slovar[key])
        print("Тренировка завершена, Ваш бонусный счет: ",bonus)
input("Введите Enter для выхода из программы\n")