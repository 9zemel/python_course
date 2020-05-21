from cars import Car
bmv = Car('bmw', 90)
jugul = Car('jigul', 120)

print(jugul.car_ride())
print(bmv.marka)
print(getattr(bmv,"speed"))
if (hasattr(jugul, "speed")):
    print('it actually rides')
else:
    print("it is broken")

print(Car.__doc__) #получение документации
print(Car.__dict__)
#
# for attr in dir(bmv):
#     if attr[0] == '_':
#         print(attr)
# for item in bmv.__dict__:
#     print(item, bmv.__dict__[item])
