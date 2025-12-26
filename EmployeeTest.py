import unittest

from Employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee module"""

    def setUp(self):
        """Create an employee for all test methods"""
        self.yemi = Employee('adeyemi','banire',300_000)

    def test_give_default_raise(self):
        """Test that default raise works correctly"""
        self.yemi.give_raise()
        self.assertEqual(305_000, self.yemi.salary)

    def test_give_custom_raise(self):
        """Test that custom raise works correctly"""
        self.yemi.give_raise(50_000)
        self.assertEqual(350_000, self.yemi.salary)


if __name__ == '__main__':
    unittest.main()
