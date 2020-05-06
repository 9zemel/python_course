def apply_discount(product, discount):
    """продукт в виде словаря
    функция возвращает имя и скидку
    """
    price = int(product['цена'] * (1.0 - discount))
    try:
        assert 0 <= price <= product['цена']
    except AssertionError:
        print('Wrong Data')
    else:
        return price, product['имя']


kreslo = {'имя': 'кресло', 'цена': 1200}
# print(apply_discount(kreslo, 0.25))
print(apply_discount(kreslo, 2.25))
