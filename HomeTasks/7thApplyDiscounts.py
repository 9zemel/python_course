# Воспользоваться кодом из нашей функции assert
# прогнать все товары в словарь из файла  data.txt
# через скидки в discount.txt
# и итоговой товар с названием и
# ценником должен генерироваться программно

file = '/Users/epolyakova/Documents/Питон/python_course/files/data.txt'
discounts = '/Users/epolyakova/Documents/Питон/python_course/files/discount.txt'


def apply_discount(product, discount):
    """продукт в виде словаря
    функция возвращает имя и финальную цену после применения скидки
    """
    price = int(product['цена']) * (1.0 - discount)

    try:
        assert 0 <= price <= int(product['цена'])

    except AssertionError:
        print('Wrong Data')
    else:
        return '{:.0f}'.format(price), product['имя']


def get_discounts_from_file(discounts):
    '''
    получение списка скидок из файла
    '''
    discs = []
    with open(discounts) as file:
        lines = file.readlines()
        for line in lines:
            discs.append(float(line.rstrip()))
    return discs


def add_products_into_dict(file):
    '''
    создание списка словарей по данным товаров из файла
    '''
    product_list = []
    with open(file) as file:
        lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i].rstrip().split(',')
        product = {'имя': line[0], 'цена': line[1]}
        product_list.append(product)
    return product_list


def search_product(name):
    '''
    поиск словаря по имени товара
    '''
    products = add_products_into_dict(file)
    for product in products:
        if product['имя'] == name:
            return product


def get_products_names(list):
    '''
    получение списка наименований товаров
    '''
    product_names = []
    list = add_products_into_dict(file)
    for discts in list:
        product_names.append(discts.get('имя'))
    return product_names


products = get_products_names(list)  # получили список товаров
discs = get_discounts_from_file(discounts)  # получили список скидок
for i in range(len(products)):
    product = search_product(products[i])
    discount = discs[i]
    result = apply_discount(product, discount)  # получили финальную цену по каждому товару
    print(result)