# Docstrings String for documentation
def hello(name):
    """
    Esto es un comentario de la funcion hello
    Imprime por pantalla un saludos concatenado con el parametro name
    :param name:
    :return:
    """
    print("Hello " + name)


hello('Jorge')

# print documentation
help(hello)


class Hello:
    """
    Clase tendra dos funciones day and bye
    Las dos reciben el parametro name
    """

    def day(self, name):
        """
        Funcion retorna buenos dias concatenado con el parametro name
        :param name:
        :return:
        """
        print("Good morning " + name)

    def bye(self, name):
        """
        Funcion retorna adios concatenado con el parametro name
        :param name:
        :return:
        """
        print("Bye " + name)


hello = Hello()
hello.bye('Jorge')

help(Hello)

help(print)
help(len)
