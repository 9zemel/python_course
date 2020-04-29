def get_full_name(name, surname, lastname):
    if lastname:
        full_name = name + ' ' + surname + " " + lastname
    else:
        full_name = name + ' ' + surname
    return full_name

name = "Галя"
surname = "Кузя"
lastname = input('Eneter your lastname')

print(get_full_name(name,surname,lastname))