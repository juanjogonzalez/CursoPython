
def hello(name = "Person"):
    print("Hola {0}".format(name))

hello("juanjo")
hello()

# def add(n1, n2):
#     return n1 + n2

# ret = add(1, 3)
# print(ret)



add = lambda n1, n2: n1+n2
ret = add(1, 3)
print(ret)