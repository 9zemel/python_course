import random

def get_name():
    name = input("Enter your name: ")
    if len(name) > 10:
        print("Wrong data")
        exit()
    return name.strip().title()

def generate_number(name):
    name_length = len(name)
    rand_str = ''
    for i in range(name_length):
        rand_num = random.randint(1, name_length)
        rand_str += str(rand_num)
    return rand_str
def get_full_data():
    name = get_name()
    number = generate_number(name)
    return name + str(number)

print(get_full_data())


