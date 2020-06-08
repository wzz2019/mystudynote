class Person:
    name:str = "default"
    gender:str = "default"
    age:int=20
    money:float=1000

    def __init__(self,name,gender,age,money):
        self.name = name
        self.name = gender
        self.name = age
        self.name = money
    def set_name(self,name):
        self.name=name

    def eat(self):
        print("is eating")
    def sleep(self):
        print("need sleep")
    def run(self):
        print("is running")

p1=Person()
p1.set_name("bob")
print(p1.name)