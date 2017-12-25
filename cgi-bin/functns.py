from heapq import nsmallest
import csv

def average(t):

    with open('lookup.csv', 'r', encoding = 'utf-8') as c:

        reader = csv.DictReader(c)

        for row in reader:

            if row['\ufeffОбъект'] == t:

                return( float( row['Средние значения, кВт*ч'].replace(',', '.') ) )

def get_rest_of_sum(total, reserved):

    """Возвращает остаток от суммы, введенной пользователем, за вычетом средств на оплату выбранных приборов.
    total - сумма, которую пользователь выделил для оплаты жкх ;
    reserved - сумма к оплате при использовании указанных пользователем приборов указанное время (вычисляет функция sum_to_pay) """    

    return total - reserved

    
def count_kvth(mtype, **kwargs):

    "Возвращает энергопотребление прибора в кВт/ч"

    if not kwargs:

        return average(mtype)
    
    mtype = mtype.strip().lower()

    if mtype == 'морозильная камера':

        return kwargs['Энергопотребление в год'] / (24*12*30)

    elif mtype == 'варочная панель':

        return sum( kwargs.values() ) * 30 / 4

    elif mtype == 'духовой шкаф':

        class2kvts = {'A+++' : 0.13, 'A++' : 0.15, 'A+' : 0.17, 'A' : 0.19, 'B' : 0.21, 'C' : 0.25, 'D' : 0.29, 'E' : 0.33}

        return class2ktvs[ kwargs['Класс энергопотребления'] ]
    
    elif mtype == 'кондиционер':

        return sum( kwargs.values() ) * 0.001 / 2

    elif mtype == 'микроволновая печь':

        return kwargs.values()[0] * 0.3

    elif mtype == 'холодильник':

        if 'Энергопотребление в год' in kwargs:

            return kwargs['Энергопотребление в год'] / (24*12*30)

        class2kvts = {(70, 'A++') :  6.79,
                      (70, 'A+') : 9.03,
                       (70, 'A') :  11.27,
                       (70, 'B') : 16.87,
                      (70, 'C') : 20.30,
                      (100, 'A++') : 9.70,
                      (100, 'A+') : 12.90,
                      (100, 'A') : 16.10,
                      (100, 'B') : 24.10,
                      (100, 'C') : 29.00,
                      (145, 'A++') : 14.07,
                      (145, 'A+') : 18.70,
                      (145, 'A') : 23.34,
                      (145, 'B') : 34.95,
                      (145, 'C') : 42.05,
                      (240, 'A++') : 19.40,
                      (240, 'A+') : 25.80,
                      (240, 'A') : 32.20,
                      (240, 'B') : 48.20,
                      (240, 'C') : 58.00,
                      (300, 'A++') : 29.10,
                      (300, 'A+') : 38.70,
                      (300, 'A') : 48.30,
                      (300, 'B') : 72.30,
                      (300, 'C') : 87.00}
        

        volume_range = min(nsmallest(2, [70,100,145,240,300] , key=lambda x: abs(x-kwargs['Полезный объем']))) if kwargs['Полезный объем'] < 300 else 300
        return class2kvts[ (volume_range, kwargs['Класс энергопотребления']) ] / (30 * 24)

    elif mtype == 'стиральная машина' or mtype == 'посудомоечная машина':

        return kwargs.values()[0]
    
    elif mtype == 'морозильная камера':

        return kwargs.values()[0] / 8760

    elif mtype in ('электрическая плита', 'тепловентилятор', 'телевизор', 'вытяжка', 'кофемашина', 'чайник'):

        return kwargs.values()[0] * 0.03
    
    else:

        return kwargs.values()[0] * 0.001
        
    

        
    
        
