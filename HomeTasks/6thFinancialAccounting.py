# дз 1.  Cделать программу финансового учета,
# которая на вход принимает файл, который ей указали,
# в котором цифры должны быть расположены построчно.
# Программа выдает простейшие статистики, такие как суммы и среднее,
# которые она записывает в файл вывода, которые она сама генерирует
# которые

import random


def get_report_path():
    report_path = input('Введите путь к файлу или его название: ').strip()
    return report_path


# report = 'report.txt' если нужно сгенерировать файл
report = get_report_path()
result = 'result.txt'


def generate_financial_data(report):
    '''
    Eсли нужно заполнить отчет сгенерированными записями
    '''
    number_of_records = 12
    nor = number_of_records
    with open(report, 'w') as file:
        for records in range(nor):
            file.write(str(random.randint(-30000, 30000)) + '\n')


def opening(report):
    '''
    открытие файла
    '''
    with open(report) as file:
        lines = file.readlines()
        return lines


def outgo(report):
    '''
    подсчет расходов
    '''
    outgo = 0
    lines = opening(report)
    for lines in lines:
        if int(lines) < 0:
            outgo += int(lines)
    return abs(outgo)


def income(report):
    '''
    подсчет доходов
    '''
    income = 0
    lines = opening(report)
    for lines in lines:
        if int(lines) > 0:
            income += int(lines)
    return income


def is_income_bigger(report):
    '''
    подсчет разницы между доходом и расходом
    '''
    total_income = income(report)
    total_outgo = outgo(report)
    diff = total_income - abs(total_outgo)
    if diff > 0:
        return '{}'.format('Доход превысил расход на ' + str(diff))
    else:
        return '{}'.format('Расход превысил доход на ' + str(abs(diff)))


def records_sum(report):
    '''
    подсчет суммы всех транзакций
    '''
    records_sum = 0
    lines = opening(report)
    for lines in lines:
        records_sum += int(lines)
    return records_sum


def records_avg(report):
    '''
    подсчет среднего значения по всем записям
    '''
    records_avg = 0
    records_sum1 = records_sum(report)
    lines = opening(report)
    number_of_records = len(lines)
    records_avg = records_sum1 / number_of_records

    return ('{:.0f}'.format(records_avg))


def write_results(result, report):
    with open(result, 'w') as file:
        file.write('Доход за отчетный период составил: ' + str(income(report)) + '\n')
        file.write('Расход за отчетный период составил: ' + str(outgo(report)) + '\n')
        file.write(str(is_income_bigger(report)) + '\n')
        file.write('Сумма всех транзакций составила: ' + str(records_sum(report)) + '\n')
        file.write('Среднее значение по всем записям: ' + str(records_avg(report)) + '\n')


def print_file(result):
    lines = opening(result)
    for line in lines:
        print(line)

# generate_financial_data(report) если нужно сгенерировать данные для отчета, а не загружать готовый файл

write_results(result, report)
print_file(result)
