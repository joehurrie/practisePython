try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
except ZeroDivisionError:
    print('age can not be zero')
except ValueError:
    print('invalid value')
