name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))
user_output = ''
whitespace = len(name.split())

if not name:
    user_output += 'Пустое имя (Enter).'
elif whitespace > 2:
    user_output += 'В имени не может быть больше одного пробела'
elif str.isspace(name):
    user_output += 'Пустое имя (пробелы).'
elif len(name) < 3:
    user_output += 'В имени не может быть менее 3 символов.'

if age <= 0:
    user_output += 'Возраст не может быть 0 или отрицательным числом'
elif age < 14:
    user_output += 'Минимальный возраст — 14 лет.'

if not user_output:
    user_output = f'Привет, {name.title()}. Тебе {age} лет! '

    if age == 16 or age == 17:
        user_output += f'Не забудь получить первый паспорт по достижению {age} лет.'
    elif age == 25 or age == 26:
        user_output += f'Не забудь заменить паспорт по достижению {age} лет.'
    elif age == 45 or age == 46:
        user_output += f'Не забудь второй раз заменить паспорт по достижению {age} лет.'

print(f'{user_output}')
