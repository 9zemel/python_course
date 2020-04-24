slovar = {}

while True:
    key = input('Enter the word in english: ').strip().lower()
    if key == 'stop':
        break
    value = input('Enter translation: ').strip().lower()
    slovar[key] = value
print(slovar)

print("Now the testing will be started, you can make only 3 mistakes\n")

errors = 0
bonus = 0

for key in slovar.keys():
    print("Enter translation for the word", key, ":")
    answer = input(":" ).strip().lower()
    if slovar[key] == answer:
        bonus += 1
        print("Your bonus score is: ", bonus)
    elif errors > 3:
        print("Game over ")
        break
    else:
        errors += 1
        print(slovar[key], "- correct answer")
        
