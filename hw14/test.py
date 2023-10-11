import unittest
import rle


class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        self.str1 = 'aaaaabbbcccc'
        self.str2 = '5a3b4c'
        self.str3 = '1aaaaabbbcccc'

    def test1(self):
        self.assertEqual(self.str2, rle.rle_encode(self.str1))

    def test2(self):
        self.assertTrue(self.str1 == rle.rle_decode(self.str2))

    def test3(self):
        self.assertRaises(ValueError, rle.rle_encode, self.str3)

    def test4(self):
        self.assertRaises(FileNotFoundError, rle.file_to_str, 'None')


if __name__ == '__main__':
    unittest.main(verbosity=True)
