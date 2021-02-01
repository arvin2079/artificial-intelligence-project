class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __eq__(self, other):
    #     return self.a == other.a

    def __lt__(self, other):
        if self.a <= other.a:
            return self

ins = A(10, 12)
print(ins.a)
ins.a = 50
print(ins.a)
#
#
# a = [
#     A(55, 14),
#     A(55, 41),
# ]
#
# a.sort()
# print(max(A(55, 14), A(55, 41)).b)
# # for i in a:
# #     print(f'a = {i.a}, b = {i.b}')

