"""
Создать класс-сущность: ExamEGE. Сделать его заглушкой.

Создать класс-дескриптор Grade (оценка). Реализовать его по новому протоколу дескрипторов.

В классе-дескрипторе реализовать перегрузку:

1) __get__ - должно возвращаться значение атрибута плюс сообщение
print(f"Вы получили доступ к оценке за экзамен по предмету: '{self.name}'")

2) __set__ - если значение атрибута не вписалось в диапазон (1-100),
аозбуждать исключение ValueError с выводом соответствующего сообщения,
Если значение вписалось - присваивать его атрибуту.

Продолжить работу над классом ExamEGE.
Создать вместо заглушки атрибуты на уровне класса. Сделать их дескрипторами (экземплярами класса Grade).
В конструктор класса при этом передвать название предмета.
Например,
math_grade = Grade('Математика')
russian_grade = Grade('Русский язык')
history_grade = Grade('История')

Проверить работу проекта на разных ситуациях с помощью клиентского кода.

Например,
math_grade = Grade('Математика')
russian_grade = Grade('Русский язык')
history_grade = Grade('История')

Проверить работу проекта на разных ситуациях с помощью клиентского кода.
"""
