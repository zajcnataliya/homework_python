# Модуль для записи результатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""  # можно в csv, можно в txt
    with open('history.csv', 'a') as h:
        h.write(f'\n{expr};{result}')


def get_history() -> list[str]:
    """Возвращает содержимое файла с результатами вычислений"""
    with open('history.csv', 'r') as h:
        return h.read()
