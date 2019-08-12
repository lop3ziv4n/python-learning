# DocTest - testing in the documentation

def add(value1, value2):
    """
    Esta funcion retorna la suma de dos parametros
    :param value1:
    :param value2:
    :return:
    >>> add(4,3)
    7
    >>> add(5,4)
    9
    >>> add(1,3)
    7
    """
    return value1 + value2


print(add(2, 4))
help(add)

import doctest

doctest.testmod()

# execute testing
# python doc_test.py -v
