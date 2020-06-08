try:
    num1=int(input("输入被除数"))
    num2=int(input("输入除数"))
    print(num1/num2)
#指定异常类型
except ZeroDivisionError:
    print('除数不能为0')
#发生未指定的异常时执行
except:
    print('发生错误')
#没有发生异常时执行
else:
    print('没有异常')
#不管有没有异常，都执行
finally:
    print('无论异常是否发生都会执行')

#在代码里主动抛出异常
# x=int(input("输入："))
# if x>10:
#     raise Exception("抛出错误")

# #继承系统的异常处理，编写自定义异常信息
# class MyException(Exception):
#     def __init__(self,value):
#         self.value=value
#         # if value==1:
#
# raise MyException("aaa")