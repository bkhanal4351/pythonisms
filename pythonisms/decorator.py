from functools import wraps

def lets_decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'some text"{orig_val}"'
    return wrapper

