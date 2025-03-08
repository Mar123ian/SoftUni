def tags(param):
    def decorator(func):
        def wrapper(*args):
            result=func(*args)
            return f"<{param}>{result}</{param}>"
        return wrapper
    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
