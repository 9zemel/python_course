slovar = {'book': 'книга', 'bear':'медведь'}
# word = input('Enter word')
slovar['floor'] = 'пол'
# for key, value in slovar.items():
#     print(key,':',value)
# for key in slovar:
#     print(key)
#     print(slovar[key])

# if 'book11' not in slovar.keys():
#     print("а перевода этого у нас и нет")

amount = input("Сколько слов в словаре?")
aow = int(amount)
slovar = {}

for i in range(aow):
    key = input("Введите слово на английском:\n ")
    value = input("Введите перевод:\n ")
    slovar[key] = value

for key in slovar.keys():
    print("Введите перевод",key,": ")
    answer = input(": ").strip().lower()
    if answer == slovar[key]:
        print("Лев доволен")
    else:
        print(slovar[key], "-правильный ответ")