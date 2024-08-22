def test_function():
    def inner_function():
        print('Я в области видимости test_function')
    inner_function() # Вызывается внутри пространства

test_function()

inner_function() # Относится к локальному пространству, вызывает ошибку "not defined"