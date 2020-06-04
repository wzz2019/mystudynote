from Animal import Animal

class cat(Animal):
    def __init__(self,color,age,sex):
        name = "猫"
        Animal.__init__(self,name,color,age,sex)
        self.hair="短毛"
    def catch_rat(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} {self.hair} 会捉老鼠")

    def shout(self):
        print(f"{self.name} {self.color} {self.age} {self.sex} {self.hair} 会喵喵叫")

if __name__=="__main__":
    cat_a=cat(color='黑色',
              age='半年的',
              sex='母的')
    cat_a.catch_rat()
    cat_a.shout()


