def arithmetic(num1, num2, operator):
    if operator == '+':
        return f'{num1 + num2}'
    if operator == "-":
        return f'{num1 - num2}'
    if operator == "*":
        return f'{num1 * num2}'


print(arithmetic(3, 2, '+'))


def seasons(month):
    if month in [1, 2, 12]:
        return f'winter'
    elif month in [3, 4, 5]:
        return f'spring'
    elif month in [6, 7, 8]:
        return f'summer'
    elif month in [9, 10, 11]:
        return f'autumn'


print(seasons(6))


def names(name, money=9000):
    return f'{name} {money}'


print(names('Ben'))
