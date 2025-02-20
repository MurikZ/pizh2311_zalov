class Person:
    def __init__(self,name,last_name,kval_spec):
        self.name = name
        self.last_name = last_name
        self.kval_spec = kval_spec
        kval_spec = 1
    def print_info(self):

        return self.kval_spec,self.name,self.last_name
    def __del__(self):
        print("До свидания мистер ",self.last_name,self.name)

first = Person("num1","numov1",1)
second = Person("num2","numov2",2)
third = Person("num3","numov3",3)
print(first.print_info())
print(second.print_info())
print(third.print_info())
del first
input()