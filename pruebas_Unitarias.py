import unittest
import CalculadoraCientifica


class TestUnitarios(unittest.TestCase):

    def test_suma1(self):
        self.assertEqual(CalculadoraCientifica.suma(-8, 4), -4)

    def test_suma2(self):
        self.assertEqual(CalculadoraCientifica.suma(10, 4), 14)

    def test_suma3(self):
        self.assertEqual(CalculadoraCientifica.suma(5, "Prueba"), 10)

    def test_resta1(self):
        self.assertEqual(CalculadoraCientifica.resta(5, 12), -7)

    def test_resta2(self):
        self.assertEqual(CalculadoraCientifica.resta(5.8, 12), -6.2)

    def test_multiplicacion1(self):
        self.assertEqual(CalculadoraCientifica.multiplicacion(3, 7), 21)

    def test_multiplicacion2(self):
        self.assertEqual(CalculadoraCientifica.multiplicacion(7, 2.5), 17.5)

    def test_division1(self):
        self.assertEqual(CalculadoraCientifica.division(35, 7), 5)

    def test_division2(self):
        self.assertEqual(CalculadoraCientifica.division(14, 4), 3.5)

    def test_raiz_cuadrada1(self):
        self.assertEqual(CalculadoraCientifica.raiz_cuadrada(9), 3)

    def test_raiz_cuadrada2(self):
        self.assertEqual(CalculadoraCientifica.raiz_cuadrada(2), 1.4142135623730951)
        
    def test_exponencial1(self):
        self.assertEqual(CalculadoraCientifica.exponencial(0), 1)

    def test_exponencial2(self):
        self.assertEqual(CalculadoraCientifica.exponencial(2), 7.389056099)


if __name__ == "__main__":
    unittest.main()
