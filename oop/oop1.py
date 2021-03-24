# class Adder:
#     def __init__(self):
#         self.sum = 0
#     def add(self, value):
#         self.sum += value
#
# acc = Adder()
# for i in range(6):
#     acc.add(i)
#
# # print(acc.sum)
#
# # print(1+2+3+4+5)
#
#
# class A(object):
#     def al(self):
#         print('al')
#
# class B(object):
#     def b(self):
#         print('b')
#         A().al()
#
# objectB= B()
# objectB.b()

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_person(self,):
        return "<person (%s, %s)>" % (self.name, self.age)

p = Person('John', 32)
print('Type of Object:', type(p), 'Memory Address:', id(p))
