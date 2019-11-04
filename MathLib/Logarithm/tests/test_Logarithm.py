import unittest
import random
from MathLib.Logarithm import Logarithm


class test_Logarithm(unittest.TestCase):
    a = random.randint(1, 65536)
    m = random.randint(1, 65536)
    # Sometimes some false assertions may become true.
    A = random.randint(1, 65536)
    M = random.randint(1, 65536)

    lg = Logarithm(m, a)
    lg1 = Logarithm(M, A)

    # TODO: Implement the tests.


if __name__ == "__main__":
    unittest.main()
