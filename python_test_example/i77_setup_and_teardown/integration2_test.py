from unittest import TestCase, main

class Integration2Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print('* Class setup')

    @classmethod
    def tearDownClass(cls):
        print('* Class clean-up')

    def setUp(self):
        print('** Test setup')

    def tearDown(self):
        print('** Test clean-up')

    def test_1(self):
        print('** Test 1')

    def test_2(self):
        print('** Test 2')

if __name__ == '__main__':
    main()
