earn = int(input("Выручка компании: "))
cost = int(input("Издержки компании: "))
if cost > earn:
    print('Убыток')
elif earn > cost:
    print('Прибыль')
    profit = (earn-cost) / earn
    print(f'Рентабельность: {profit}')
    workers = int(input('Количество сотрудников: '))
    profit_per_worker = (earn - cost) / workers
    print(f'Прибыль в расчете на одного сотрудника составила: {profit_per_worker}')
