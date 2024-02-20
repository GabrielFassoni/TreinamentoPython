class Calculadora:
    def __init__(self):
        self.resultado = 0

    def adicao(self, num1, num2):
        self.resultado = num1 + num2

    def subtracao(self, num1, num2):
        self.resultado = num1 - num2

    def divisao(self, num1, num2):
        self.resultado = num1 / num2

    def multiplicacao(self, num1, num2):
        self.resultado = num1 * num2

    def exibir_resultado(self):
        print(self.resultado)


calculadora = Calculadora()
calculadora.adicao(num1=10, num2=20)
calculadora.exibir_resultado()
