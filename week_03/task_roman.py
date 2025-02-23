class Roman:

    def __init__(self, arg_plus,arg_minus,arg_umn, arg_del):
        self.arg_plus = arg_plus
        self.arg_minus = arg_minus
        self.arg_umn = arg_umn
        self.arg_del = arg_del


    def __add__(self, other):
        return self.arg_plus + other


    def __sub__(self, other):
        return self.arg_minus - other

    def __mul__(self, other):
        return self.arg_umn * other

    def __truediv__(self, other):
        return self.arg_del / other
a = Roman(3,3,4,5)
print(a.__add__(4))
print(a.__mul__(4))
print(a.__sub__(4))
print(a.__truediv__(4))





