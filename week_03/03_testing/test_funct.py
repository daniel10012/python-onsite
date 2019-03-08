import unittest
from funct import inv

'''the first function, inv, is going to return the inverse of the sum of 2 numbers : 1/(x+y)'''

class TestCustomfun(unittest.TestCase):

    def test_return_none_if_inputs_are_strings(self):
        self.assertEqual(inv(1,2), 1/3)





if __name__ == '__main__':
    unittest.main()
