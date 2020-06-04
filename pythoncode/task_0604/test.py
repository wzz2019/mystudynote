def aa():
    aa=1
    print(f"this is aa: {aa}")
    return aa
def a():
    a=1
def bb():
    bb=1
    cc=bb*10
    print(f"this is bb: {bb}")
    print(f"this is cc（=bb*10）: {cc}")
    return bb

def c(a,b):
    c=a+b
    print(f"this is a: {a}")
    print(f"this is b: {a}")
    print(f"this is c（a+b）: {c}")

aa()
bb()
c(aa(),bb())
#方法无默认值时，返回"None",是“NoneType”
print("no return is:"+str(a()))