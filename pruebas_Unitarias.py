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


if __name__ == "__main__":
    unittest.main()
