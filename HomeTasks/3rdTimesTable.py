#Вывести полную таблицу умножения, вместе с числами, которые учавствуют в операции в таком виде:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# И так далее

arr_numbers = [[], [], []]

for i in range(2, 10):
    for j in range(1, 10):
        arr_numbers[0].append(i) #отдельно множители 1
        arr_numbers[1].append(j) #отдельно множители 2
        arr_numbers[2].append(i * j) #произведение

count = 0 #число записей
mnojitel = arr_numbers[0].count(arr_numbers[0][0]) #множитель

for k in range(len(arr_numbers[0])):
    print(arr_numbers[0][k], '*', arr_numbers[1][k], '=', arr_numbers[2][k])
    count += 1
    if count % mnojitel == 0: #если число записей кратно множителю таблицы, время табуляци для нового столбца
        print('\t')