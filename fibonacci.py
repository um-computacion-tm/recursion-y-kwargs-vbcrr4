import unittest

def fibonacci (num):
    '''if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)'''
    resultado, anterior = 0,1
    for _ in range(num):
        anterior,resultado = resultado,anterior + resultado
    return resultado

class TestFibonacci(unittest.TestCase):

    def test_caso_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_caso_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_caso_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_caso_4(self):
        self.assertEqual(fibonacci(4), 3)

    def test_caso_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_caso_6(self):
        self.assertEqual(fibonacci(6), 8)

    def test_caso_7(self):
        self.assertEqual(fibonacci(7), 13)

    def test_caso_8(self):
        self.assertEqual(fibonacci(8), 21)

    def test_caso_9(self):
        self.assertEqual(fibonacci(9), 34)

    def test_caso_10(self):
        self.assertEqual(fibonacci(10), 55)

    def test_caso_11(self):
        self.assertEqual(fibonacci(11), 89)

    def test_caso_12(self):
        self.assertEqual(fibonacci(12), 144)

    def test_caso_13(self):
        self.assertEqual(fibonacci(13), 233)

    
if __name__ == '__main__':
    unittest.main()