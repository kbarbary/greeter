"""
Unit tests for Greeter class
"""
import unittest
import os
import greeter

class GreeterUnitTestCase(unittest.TestCase):

    def setUp(self):
        "Create a Greeter object to be used in each of the tests."
        self.Jeeves = greeter.Greeter()

    def tearDown(self):
        "Clean up any mock data files created by the tests."
        if self.Jeeves.outputs is not None:
            for file in self.Jeeves.files:
                try:
                    os.remove(file)
                except:
                    pass

    def test_greet(self):
        self.Jeeves.greet()
        self.assertEquals(self.Jeeves.message, "hello world!")


if __name__ == '__main__':
    unittest.main()
