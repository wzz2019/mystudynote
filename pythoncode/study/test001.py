#局部变量：函数内部不可调用外部变量
#函数内部定义的变量，也不会修改函数外的同名变量
#函数内部修改外部全局变量，函数执行完，外部的全局变量仍是原值
#函数内需要修改变量，需要在函数内定义为全局变量
a=1
global b
b=1
def fun():
#    print(a)
    global a,b
    a=2
    print(f"a={a}")
    b=2
    print(f"b={b}")

fun()
print(f"a={a}")
print(f"b={b}")