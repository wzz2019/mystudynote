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

if __name__=="__main__":
    animal_a=Animal(name="兔子",
                    color="白色",
                    age="3个月大",
                    sex="公的")
    animal_a.run()
    animal_a.shout()
