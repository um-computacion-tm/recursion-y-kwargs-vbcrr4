import unittest

def sumatoriawhile(value):
    resultado = 0
    while value > 0:
        resultado += value
        value -= 1
    return resultado

def sumatoriarecursive(numero):
    if numero <= 0:
        return 0  # Caso base para la recursión
    return numero + sumatoriarecursive(numero - 1)

class TestSumatoriaRecursive(unittest.TestCase):
    def test_sumatoria(self):
        numero = 4
        totalsum = sumatoriarecursive(numero)
        self.assertEqual(totalsum, 10)

class TestSumatoriawhile(unittest.TestCase):
    def test_sumatoria2(self):
        numero = 4
        totalsum = sumatoriawhile(numero)
        self.assertEqual(totalsum, 10)

    def test_sumatoria3(self):
        numero = 6
        totalsum = sumatoriawhile(numero)
        self.assertEqual(totalsum, 21)

if __name__ == '__main__':
    unittest.main()
