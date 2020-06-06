"""
类的继承，方法重写
"""
class Animal():
    def __init__(self,name,color,age,sex):
        self.name=name
        self.color=color
        self.age=age
        self.sex=sex

    def get_decrib(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} ")

class Cat(Animal):
    def __init__(self,color,age,sex):   #定义自己的构造函数
        name = "猫"
        Animal.__init__(self,name,color,age,sex)    #调用父类的构造函数
        self.hair="短毛"

    def get_decrib(self):       #覆写父类的方法
        print(f"{self.name} {self.color} {self.age} {self.sex}  {self.hair}")

if __name__=="__main__":
    animal_a=Animal(name="兔子",color="白色",age="3个月大",sex="公的")
    animal_a.get_decrib()

    cat_a=Cat(color='黑色',age='3岁了', sex='母的')
    cat_a.get_decrib()
