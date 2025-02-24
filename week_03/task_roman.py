class Roman:
    def __init__(self, arg_plus, arg_minus, arg_umn, arg_del, roman_numbers)->None:
        self.arg_plus = arg_plus
        self.arg_minus = arg_minus
        self.arg_umn = arg_umn
        self.arg_del = arg_del
        self.roman_numbers = roman_numbers



    def roma(self, number)->str:
        num = ''
        for key, value in self.roman_numbers.items():
            while number >= value:
                num += key
                number -= value
        return num

    def __add__(self, other)->int:
        return self.arg_plus + other


    def __sub__(self, other)->int:
        return self.arg_minus - other

    def __mul__(self, other)->int:
        return self.arg_umn * other

    def __truediv__(self, other)->int:
        return self.arg_del / other
roman = Roman(3,5,4,5,{'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                     'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                     'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1})
plus = roman.__add__(4)
minus = roman.__sub__(4)
umnozhit = roman.__mul__(4)
razdelit = roman.__truediv__(4)

print(roman.roma(plus))
print(roman.roma(minus))
print(roman.roma(umnozhit))
print(roman.roma(razdelit))