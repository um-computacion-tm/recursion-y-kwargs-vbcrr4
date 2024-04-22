import unittest
def factorial (valor): #resolver problemas con for y con while
    '''resultado = num1
    while num1 >= 1:
        num1 = num1 - 1
        resultado = factorial(1)'''
    #condicion de corte
    if valor in  (0,1):  # ** diccionario de parametros nombrados, * lista de parametros variables
        return 1
    if valor <= 0:
        return "debe ingresar valores positivos"
    #llamada recursiva
    return valor * factorial(valor - 1)

class TestFactorial(unittest.TestCase):
    def test_caso_negativo(self):
        resultado = factorial(-1)
        self.assertEqual(resultado,"debe ingresar valores positivos")

    def test_caso_0(self):
        resultado = factorial(0)
        self.assertEqual(resultado,1)

    def test_caso_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado, 1)
    
    def test_caso_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)
    
    def test_caso_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)

    def test_caso_4(self):
        resultado = factorial(4)
        self.assertEqual(resultado, 24)
    
    def test_caso_5(self):
        resultado = factorial(5)
        self.assertEqual(resultado, 120)
    
    def test_caso_6(self):
        resultado = factorial(6)
        self.assertEqual(resultado, 720)


    def test_caso_7(self):
        resultado = factorial(7)
        self.assertEqual(resultado,5040)

if __name__ == '__main__':
    unittest.main()