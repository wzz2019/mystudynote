class Animal():
    def __init__(self,name,color,age,sex):
        self.name=name
        self.color=color
        self.age=age
        self.sex=sex

    def run(self):
        print("会跑")

    def shout(self):
        print("会叫")