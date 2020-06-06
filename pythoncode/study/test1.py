#计算1~100求和
result=0
for i in range(1,101):
    result=result+i
print(result)
#计算1~100的偶数求和
result=0
for i in range(1,101):
    if i%2==0:
        result=result+i
print(result)
#计算1~100的偶数求和
result=0
for i in range(2,101,2):
    result=result+i
print(result)