# singleton definition
# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance

# s = Singleton()
# print("object created", s)

# s1 = Singleton()
# print("object created", s1)

# lazy initialize
# class Singleton(object):
#     __instance = None
#     def __init__(self):
#         if not Singleton.__instance:
#             print("__init__ method called..")
#         else:
#             print("Instance already created:", self.getInstance())
#     @classmethod
#     def getInstance(cls):
#         if not cls.__instance:
#             cls.__instance = Singleton()
#         return cls.__instance

# s = Singleton()
# print("object created", Singleton.getInstance())
# s1 = Singleton()

# monostate
# class Borg:
#     __shared_State = {'1':'2'}
#     def __init__(self):
#         self.x = 1
#         self.__dict__ = self.__shared_State
#         pass

# b = Borg()
# b1 = Borg()
# b.x = 4

# print("Borg Object 'b': ", b)
# print("Borg Object 'b1': ", b1)
# print("Object state 'b': ", b.__dict__)
# print("Object state 'b1': ", b1.__dict__)

#use __new__
# class Borg(object):
#     _shared_State = {}
#     def __new__(cls, *args, **kwargs):
#         obj = super(Borg, cls).__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls._shared_State
#         return obj

import transformers

@classmethod(f)