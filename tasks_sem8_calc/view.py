# Модуль для ввода/вывода информации


def choose() -> str:
    """Выбор режима работы приложения"""
    print('1 - solve expression\n\
2 - solve equasion\n\
3 - simplify polinom\n\
4 - show history')
    return input('Choose mode: ')


def get_expr() -> str:
    """Запрашивает у пользователя задачу"""
    return input('Enter exspression: ')


def show_res(res: str):
    """Выводит результат"""
    print(res)


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    print('Такого режима нет')


def show_history(history: str):
    """Выводит историю операций"""
    # print(history.split('\n'))
    for i in history.split('\n'):
        print(i.replace(';', ' -> result: '))
