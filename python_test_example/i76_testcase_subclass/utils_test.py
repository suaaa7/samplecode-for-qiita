from unittest import TestCase, main

from i76_testcase_subclass.utils import concat

class UtilsTestCase(TestCase):
    def test_good_for_concat(self):
        test_cases = [
            (('a', 'b'), 'ab'),
            (('test', 'case'), 'testcase'),
        ]
        for value, expected in test_cases:
            with self.subTest(value):
                self.assertEqual(expected, concat(value[0], value[1]))

    def test_bad_for_concat(self):
        test_cases = [
            (('a', 2), TypeError),
            ((1, 'b'), TypeError),
        ]
        for value, exception in test_cases:
            with self.subTest(value):
                with self.assertRaises(exception):
                    concat(value[0], value[1])

if __name__ == '__main__':
    main()
