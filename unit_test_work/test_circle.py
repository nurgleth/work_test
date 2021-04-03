import unittest
from math import pi

from circle import circle_area


# чтобы запустить юнит тест в консоле прописать python -m unittest test_circle.py

class TestCircArea(unittest.TestCase):
    def test_area(self):  # чтобы система понимала что именно необходимо считать тестами метод называем с препиской test
        self.assertEqual(circle_area(3), pi * 3 ** 2)  # проверяем работает ли вообще функция, равенство значений
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(2.5), pi * 2.5 ** 2)

    def test_values(self):  # выбрасываются ли исключения для отрициательных радиусов
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, -1)

    def test_types(self):  # выбрасывается исключения если некоректный тип данных
        self.assertRaises(TypeError, circle_area, 5 + 3j)
        self.assertRaises(TypeError, circle_area, [])
        self.assertRaises(TypeError, circle_area, [43, 2])
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "tru")


if __name__ == '__main__':
    unittest.main()
