def validate_name(name: str):
    whitespace = len(name.split())
    if not name:
        return 'Пустое имя (Enter).'
    if whitespace > 2:
        return 'В имени не может быть больше одного пробела'
    if str.isspace(name):
        return 'Пустое имя (пробелы).'
    if len(name) < 3:
        return 'В имени не может быть менее 3 символов.'
    return ''


def validate_age(age: int):
    if age <= 0:
        return 'Возраст не может быть 0 или отрицательным числом'
    if age < 14:
        return 'Минимальный возраст — 14 лет.'
    return ''


def validate_age_passport(age: int):
    passport_age = ''
    if age == 16 or age == 17:
        passport_age += f'Не забудь получить первый паспорт по достижению {age} лет.'
    if age == 25 or age == 26:
        passport_age += f'Не забудь заменить паспорт по достижению {age} лет.'
    if age == 45 or age == 46:
        passport_age += f'Не забудь второй раз заменить паспорт по достижению {age} лет.'
    return passport_age


def main():
    while True:
        name = input('Введите Ваше имя: ')
        age = int(input('Введите Ваш возраст: '))
        if validate_name(name) == '' and validate_age(age) == '':
            user_output = f'Привет, {name.title()}. Тебе {age} лет! {validate_age_passport(age)}'
            print(f'{user_output}')
            break
        elif not validate_name(name) == '':
            user_output = validate_name(name)
        elif not validate_age(age) == '':
            user_output = validate_age(age)
        else:
            continue
        return print(f'{user_output}')


main()
