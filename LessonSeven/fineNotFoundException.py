def count_words(filename):
    '''Считает кол-во строк в файле'''
    try:
        with open(filename, encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f" В этом {filename} около {num_words} слов")

filenames = ['book1.txt', 'book2', 'book3']

for file in filenames:
    count_words(file)
