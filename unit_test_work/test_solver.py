import unittest

from solver import add, square_equation_solver


# def test_ok():
#     res = add(1, 2)
#     assert res == 3


class TestSquarEquationSolver(unittest.TestCase):
    def test_raises_type_error(self):
        with self.assertRaises(TypeError):  # проверяем поднята ли ошибка
            square_equation_solver("", 1, 1.5)

    def test_result_is_tuple(self):  # проверям принаждлежность к типу, должен вернуться кортеж
        res = square_equation_solver(0, 0, 0)
        self.assertIsInstance(res, tuple)

    def test_no_results(self):
        res = square_equation_solver(0, 0, 1)
        self.assertEqual(res, (None, None))

    def test_solves_ok(self):
        res = square_equation_solver(1, -3, -4)
        self.assertEqual(res, (4, -1))



