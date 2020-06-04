class Animal():

    def __init__(self,name,color):
        self.name=name
        self.color=color
        # self.age=age
        # self.sex=sex

    def run(self):
        print(f"{self.color}的{self.name}会跑")

    def shout(self):
        print(f"{self.color}的{self.name}会叫")
