"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别提示：
大了/小了/猜对了
"""
import random

number=random.randint(1,100)
while True:
    input_num=int(input("请输入一个数字："))
    if input_num>number:
        print("大了")
    elif input_num<number:
        print("小了")
    else:
        print("猜对了 O(∩_∩)O")
        break

