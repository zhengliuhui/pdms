import logging
def use_logging(level):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if level=="warn":
                logging.warn("%s is running" % func,__name__)
        return wrapper
    return decorator
@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)
foo()