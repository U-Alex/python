from unittest import TestCase
from parameterized import parameterized
from c_list import CustomList
from c_compare import compare


class TestCustomList(TestCase):
    """тест класса CustomList"""

    def test_custom_list_error_not_list(self):
        """создание экземпляра с неверным параметром, не list"""
        self.assertRaises(TypeError, CustomList, "1, 2, 3, 4, 5, 6")

    def test_custom_list_error_not_int(self):
        """создание экземпляра с неверным типом данных, не int"""
        self.assertRaises(TypeError, CustomList, ['1', '2', '3', 4, 5, 6])

    @parameterized.expand([
        ([1, 2, 3, 4, 5, 6], 3.5),
        ([-1, -2, -3, -4, -5, -6], -3.5),
        ([], None),
    ])
    def test_custom_list_average(self, param, result):
        """создание экземпляра с допустимыми параметрами"""
        test_list = CustomList(param)
        self.assertEqual(test_list.average, result)

    def test_custom_list_str(self):
        """проверка дандер-метода __str__"""
        test_list = CustomList([1, 2, 3, 4])
        self.assertEqual(test_list.__str__(), '1, 2, 3, 4')

    # def test_CustomList_average_none(self):
    #     test_list = CustomList([])
    #     self.assertEqual(test_list.average, None)


class TestCompare(TestCase):
    """тест модуля сompare"""

    def test_compare_list1_none(self):
        """проверка с допустимыми параметрами, но с одним пустым списком"""
        test_result = compare([], [3, 4, 5, 6, 7, 8])
        self.assertEqual(test_result, "Один из списков пуст")

    def test_compare_list2_none(self):
        """проверка с допустимыми параметрами, но с одним пустым списком"""
        test_result = compare([3, 4, 5, 6, 7, 8], [])
        self.assertEqual(test_result, "Один из списков пуст")

    def test_compare_list1_qt(self):
        """проверка с допустимыми параметрами, 1 рабочий сценарий"""
        test_result = compare([3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6])
        self.assertEqual(test_result, "Первый список имеет большее среднее значение")

    def test_compare_list2_qt(self):
        """проверка с допустимыми параметрами, 2 рабочий сценарий"""
        test_result = compare([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8])
        self.assertEqual(test_result, "Второй список имеет большее среднее значение")

    def test_compare_list1_equals(self):
        """проверка с допустимыми параметрами, 3 рабочий сценарий"""
        test_result = compare([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
        self.assertEqual(test_result, "Средние значения равны")

    def test_compare_error_not_list(self):
        """проверка с неверным параметром, не list"""
        self.assertRaises(TypeError, compare, ("1, 2, 3, 4, 5, 6", []))

    def test_compare_error_not_int(self):
        """проверка с неверным типом данных, не int"""
        self.assertRaises(TypeError, compare, (['1', '2', '3', 4, 5, 6], []))
