full_path = '/Users/epolyakova/Documents/Питон/python_course/LessonSixth/files2/words.txt'

negative_words = ['дрянной','дрянное','дрянная']

with open(full_path) as file:
    lines = file.readlines()
    for line in lines:
        for word in negative_words:
            if line.strip() == word:
                print('censored')
                break
            print(line.lstrip())
            break
    print(len(lines))