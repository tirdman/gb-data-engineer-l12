"""
Создать класс-сущность: MyClass. Сделать его заглушкой.

Создать класс-дескриптор TypedProperty. Реализовать его по новому протоколу дескрипторов.

В классе-дескрипторе реализовать перегрузку:
1) __set__ - проверяет относится ли присваиваемое значение к типу данных, указанному
и переданному в конструктор класса-дескриптора
Если не относится, возбуждать исключение TypeError
с выводом сообщения "Значение должно быть типа {self.type}"
Если относится, присвоить значение атрибуту.

2) __delete__ - при попытке удаления атрибута давать исключение
AttributeError с выводом соответствующего сообщения.

Продолжить работу над классом MyClass.
Создать вместо заглушки атрибуты на уровне класса. Сделать их дескрипторами (экземплярами класса TypedProperty).
В конструктор класса при этом передвать тип данных

Например,
name = TypedProperty(str)

Проверить работу проекта на разных ситуациях с помощью клиентского кода..
"""
