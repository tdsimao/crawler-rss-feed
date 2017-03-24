import unittest


class SimpleTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_equal(self):
        self.assertEqual("", "")

if __name__ == '__main__':
    unittest.main()
