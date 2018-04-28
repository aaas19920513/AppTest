
def log(func):
    def wrapper():
        print 'call %s():' % func.__name__
        return func()
    return wrapper

def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log1('hello')
def now():
    print '2013-12-25'

now()

