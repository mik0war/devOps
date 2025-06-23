from functools import wraps


def handle_errors(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except (KeyError, TypeError):
            return 'Неверные входные данные'

    return wrapped

@handle_errors
def plus(a, b):
    return a + b

@handle_errors
def minus(a, b):
    return a - b

@handle_errors
def mul(a, b):
    return a * b

@handle_errors
def div(a, b):
    if b == 0:
        return 'Деление на 0'

    return a / b

