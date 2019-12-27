# def foo(*args):
#     return sum(args) / len(args)
# print(foo(10,20,30,40))

# def word(*args):
#     args = [x.upper() for x in args]
#     return sorted(args)
# print(word("ice", "snow", "glacier"))

# keyword argument
def find_sum(**kwargs):
    return sum(kwargs.values())
print(find_sum(x=4, y=3, z=2))