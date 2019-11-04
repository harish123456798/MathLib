import unittest
import random
from MathLib.AP import AP


class test_AP(unittest.TestCase):
    a = random.randint(-65536, 65536)
    d = random.randint(-65536, 65536)
    N = random.randint(1, 65536)
    ap = AP(a, d)

    def test_first_term(self):
        self.assertEqual(self.a, self.ap.a)

    def test_difference(self):
        ap1 = self.ap.nth_term(4)
        ap2 = self.ap.nth_term(5)
        self.assertEqual(ap2 - ap1, self.d)

    def test_next_term(self):
        ap1 = self.ap.next_term()
        self.assertEqual(ap1, self.a + self.d)

    def test_sum_n_terms(self):
        self.assertEqual((self.N/2*(2*self.a+(self.N-1) * self.d)),
                         self.ap.sum_n_terms(self.N))


if __name__ == "__main__":
    unittest.main()
