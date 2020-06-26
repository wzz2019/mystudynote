x=(1,2,3)
y=(["a","b"],[1,2])

def a(*x):
    print(x)
    print(type(x))
def b(x):
    print(x)
    print(type(x))
def c(*x):
    print(*x)
    print(type(*x))



a(x)
b(x)
c(x)
a(y)
b(y)
c(y)