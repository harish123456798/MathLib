from __future__ import annotations
import math

__all__ = ["Logarithm"]


class Logarithm:
    """
    Let there be a number "A" > 0 and A != 1. Then if "A" and "M" are so related
    that A ^ x = M, then x is called the logarithm of M to the base "A".
    """

    def __init__(self, M: float, A: float = 10):
        """
        @param A: Base.
        @param M: The number of which we want to logarithm to the base A''
        """
        self.a = A
        self.m = M

    def __repr__(self):
        return str(math.log(self.m, self.a))

    def __add__(self, additive: Logarithm):
        return (float(self.__repr__()) + float(additive.__repr__()))

    def __sub__(self, subtractive: Logarithm):
        return (float(self.__repr__()) - float(subtractive.__repr__()))

    def __mul__(self, multiplier: Logarithm):
        if self.a == multiplier.a:
            return (float(self.__repr__()) + float(multiplier.__repr__()))
        else:
            raise NotImplementedError("Not Allowed")

    def __truediv__(self, divisor: Logarithm):
        if self.a == divisor.a:
            return (float(self.__repr__()) - float(divisor.__repr__()))
        else:
            raise NotImplementedError("Not Allowed")

    def __pow__(self, N: float):
        return (N * float(self.__repr__()))
