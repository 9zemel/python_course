name = input("Enter you diary's name")

with open(name, 'a') as diary:
    data = input('Enter your topic:\n')
    diary.write(data)

