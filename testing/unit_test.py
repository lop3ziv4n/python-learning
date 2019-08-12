# UnitTest - testing in the code
def multi(value1, value2):
    return value1 * value2


print(multi(2, 4))

import unittest


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(multi(2, 4), 8)
        self.assertEquals(multi(2, 4), 9)


if __name__ == '__main__':
    unittest.main()
