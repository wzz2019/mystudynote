class Animal():
    def __init__(self,name,color,age,sex):
        self.name=name
        self.color=color
        self.age=age
        self.sex=sex

    def run(self):
        print(f"{self.name} can run")

    def shout(self):
        print(f"{self.name} can shout")