def sum_to_pay(energy_and_hours, n, r, nr):
    
    """Вычисляет сумму к оплате исходя из энергопотребления выбранных пользователем товаров и времени их работы.
Для разработчика сайта: в переменную energy_and_hours передается список вида [(эн/потр_1, (время_день, время_ночь, время_полупик) ),.., (эн/потр_N, (время_день, время_ночь, время_полупик) )]
Длина тупла с часами зависит от "ставочности" счетчика.
Например, если у пользователя двухставочный счетчик, прибор 1 потребляет 0,15 кВт/ч, работает днем 4 часа, ночью 30 минут,
а прибор 2 потребляет 1 кВт/ч и работает 2 часа днем и 2 - ночью, вход выглядит так:
energy_and_hours = [(0.15, (4, 0.5)), (1, (2,2))]"""
    
    if len(energy_and_hours[0][1]) == 0: #если счетчика нет
        return nr*r[0][0]*people
            
    if len(energy_and_hours[0][1]) == 1:
        q = sum([tup[0] * tup[1][0] for tup in energy_and_hours])
        if q > n:
            total = round(n*r[0][0] + (q-n)*r[1][0],2)
        else:
            total = round(q*r[0][0],2)
            
    elif len(energy_and_hours[0][1]) == 2: #для двуставочного счетчика
        q_day , q_night = sum([tup[0] * tup[1][0] for tup in energy_and_hours]), sum([tup[0] * tup[1][1] for tup in energy_and_hours])
        if (q_day + q_night) > n:
            M1, v1 = numpy.array([[1., 1.], [q_day, -q_night]]), numpy.array([n,0.])
            counts = numpy.linalg.solve(M1, v1)
            total = round(counts[0]*r[1][0] + counts[1]*r[2][0] + (q_day-counts[0])*r[1][1] + (q_night-counts[1])*r[2][1],2)
        else:
            total = round(q_day*r[1][0] + q_night*r[2][0],2)
            
    else: #для трехставочного счетчика
        q_peak, q_semipeak, q_night = sum([tup[0] * tup[1][0] for tup in energy_and_hours]), sum([tup[0] * tup[1][1] for tup in energy_and_hours]), sum([tup[0] * tup[1][2] for tup in energy_and_hours])
        if (q_peak + q_semipeak + q_night) > n: #если потреблено > соц.нормы
            M1 = numpy.array([[1., 1., 1.], [q_semipeak, q_night-q_peak, -q_semipeak],
                    [q_night+q_semipeak, -q_peak, -q_peak], [q_night, q_night, -q_peak-q_semipeak]]) 
            v1 = numpy.array([n,0.,0.,0.])
            counts = numpy.linalg.lstsq(M1, v1)
            counts = counts[0]
            total = round(counts[0]*r[3][0] + counts[1]*r[4][0] + counts[2]*r[5][0] + (q_peak-counts[0])*r[3][1] + 
                     (q_semipeak-counts[1])*r[4][1] + (q_night-counts[2])*r[5][1],2)
        else: #если потреблено < соц.нормы
            total = round(q_peak*r[3][0] + q_semipeak*r[4][0] + q_night*r[5][0],2)

    return total
