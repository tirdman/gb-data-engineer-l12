"""
Задание 3.

В этом задании мы применим и дескриптор, и метакласс.

1. Реализовать класс-дескриптор TypedProperty.
В нем нужно перегрузить метод __set__, в котором делаем валидацию,
в которой проверяем, что присваиваемое значение относится к переданному
также в __set__ типу данных. Если не относится даем исключение.
Если относится, нужно обратиться к слотам экземпляра подчиненного класса
и через append добавить нужное значение в атрибуты.

2. Реализовать метакласс TypedMeta
В нем сделать перегрузку метода __new__
В нем перебирать атрибуты подчиненного класса
и на предмет, является ли очередной атрибут экземпляром TypedProperty
isinstance(value, TypedProperty)
и если да, вносим атрибут в слоты.

3. Наконец, сделать подчиненный метаклассу класс MyClass
class MyClass(metaclass=TypedMeta):
    ''' Пользовательский класс с контролируемыми атрибутами
    '''
    name = TypedProperty(str)
    num = TypedProperty(int)
    zzz = 15
    xxx = 17

Потестить операции с атрибутами его экземпляра, увидеть разницу
"""