class Animal():
    def __init__(self,name,color,age,sex):
        self.name=name
        self.color=color
        self.age=age
        self.sex=sex

    def run(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} 会跑")

    def shout(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} 会叫")

class Cat(Animal):
    def __init__(self,color,age,sex):
        name = "猫"
        Animal.__init__(self,name,color,age,sex)
        self.hair="短毛"

    def catch_rat(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} {self.hair} 会捉老鼠")
    #覆写父类的方法
    def shout(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} {self.hair} 会喵喵叫")

class Dog(Animal):
    def __init__(self,color,age,sex):
        name = "狗"
        Animal.__init__(self,name,color,age,sex)
        self.hair="长毛"

    def watch_home(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} {self.hair} 会捉老鼠")
    def shout(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} {self.hair} 会喵喵叫")

if __name__=="__main__":
    animal_a=Animal(name="兔子",color="白色",age="3个月大",sex="公的")
    animal_a.run()
    animal_a.shout()

    cat_a=Cat(color='黑色',age='3岁了', sex='母的')
    cat_a.catch_rat()

    dog_a=Dog(color='黄色',age='一岁了', sex='公的')
    dog_a.watch_home()
    print(f"{dog_a.name} {dog_a.color} {dog_a.age} {dog_a.sex} {dog_a.hair}")
