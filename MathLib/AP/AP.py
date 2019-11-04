from __future__ import annotations

__all__ = ["AP"]


class AP:
    """
    Arithmetic Progression is a sequence in which each term,
    except the first term is obtained by adding a fixed number,
    to the term immediately it.
    """

    def __init__(self, A: float = 0, D: float = 1):
        """
        @param A: First term of the AP.
        @param D: The common difference between consecutive terms of the AP.
        """
        self.a = A
        self.d = D
        self._n = 1  # A is the first term of the AP.

    def nth_term(self, N: int):
        if N == 1:
            return self.a
        else:
            return (self.a + (N - 1) * self.d)

    def next_term(self):
        if self._n == 1:
            self._n += 1
            return self.nth_term(self._n)
        else:
            self._n += 1
            return self.nth_term(self._n)

    def sum_n_terms(self, N):
        return (N / 2 * (2 * self.a + (N - 1) * self.d))
