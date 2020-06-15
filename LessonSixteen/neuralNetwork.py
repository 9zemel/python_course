import random
import math

inches = 40 #у нас 40 дюймов
centimetre = 101.6

def kid_neuro(epoch, lr, accur):
    '''
    :param epoch: сколько раз попробует подобрать
    :param lr: ширина шага
    :param accur: точность результата
    :return:
    '''
    W_coef = random.uniform(1,3)
    print(f"Наш первоначальный вес равен: {W_coef}")

    for i in range(epoch):
        Error = centimetre - (inches * W_coef)
        print(f"Наша ошибка составляет {Error}")

        if abs(Error) < accur:
            print(f"Наш итоговый результкт {W_coef}")
        if Error > 0:
            W_coef += lr
        elif Error < 0:
            W_coef -= lr
            #если ошибка отрицательная, нужно уменьшать вес

