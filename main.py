try:
    salary = float(input('Salary->'))
    # 1 - 700 : 5%        | 1 <= salary <= 700
    # 701 - 1000 : 7%     | 700 < salary <= 1000
    # 1001 and more : 10% | 1000 < salary
    result_salary = float(0)
    perc = 0
    if 1 <= salary <= 700:
        perc = 5
    elif 700 < salary <= 1000:
        perc = 7
    elif 1000 < salary:
        perc = 10
    else:
        raise Exception('Unknown operation.')
    formula = ((salary/100) * perc)
    result_salary = salary - ((salary/100) * perc)
    print(f'{salary}$ - {perc}%({formula}) = {result_salary}$')
except Exception as e:
    print(e)
print('Exit...')


