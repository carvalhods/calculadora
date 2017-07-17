class Operacoes(object):
    
    __num1 = 0
    __num2 = 0

    def __init__(self, num1, num2):
        self.__num1 = int(num1)
        self.__num2 = int(num2)

    def somar(self):
        return self.__num1 + self.__num2

    def subtrair(self):
        return self.__num1 - self.__num2

    def multiplicar(self):
        return self.__num1 * self.__num2

    def dividir(self):
        return self.__num1 / self.__num2
