#  Copyright (c) 2022. Generated by Gu.
class A:
    v = 0

    @classmethod
    def get_v(cls):
        return cls.v

    @classmethod
    def set_v(cls, value):
        cls.v = value


print(A.get_v())
A.v = 100
print(A.get_v())
