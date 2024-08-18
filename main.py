def test_function():
    inner_function()


def inner_function():
    def new_function():
        print('Я в области видимости функции test_function')
    new_function()


test_function()