day = int(input('What a day? '))
try:
    if day > 31:
        raise ValueError("It's too big")
except ValueError as msg:
    # exit()
    print("Программа нашла", msg)
finally:
    print(f'Классная погода {day} числа')