def test_function():
    def inner_function():
        print( "Я в области видимости функции test_function")

test_function()

#inner_function()

#NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
#innerfunction доступна только в области видимости testfunction