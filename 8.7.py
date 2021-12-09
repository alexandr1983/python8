class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return f"z = {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i"'"

    def __str__(self):
        return f"z = {self.a} + {self.b} * i"

a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
z_1 = Complex(a1, b1)
z_2 = Complex(a2, b2)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
