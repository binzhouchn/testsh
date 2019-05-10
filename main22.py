
import os
print(os.getcwd())


class A:
    def __init__(self):
        pass

    def ff(self, x):
        return x + 5


def ff(x):
    return x ** 2


print(ff(10))
print(A().ff(10))