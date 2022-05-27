import unittest
import CalculadoraCientifica


class TestUnitarios(unittest.TestCase):

    def test_suma1(self):
        self.assertEqual(CalculadoraCientifica.suma(-8, 4), -4)

    def test_suma2(self):
        self.assertEqual(CalculadoraCientifica.suma(10, 4), 14)

    def test_suma3(self):
        self.assertEqual(CalculadoraCientifica.suma(5, "Prueba"), 10)


if __name__ == "__main__":
    unittest.main()
