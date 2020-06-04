from Animal import Animal

class cat(Animal):
    def __init__(self,name,color,age,sex):
        Animal.__init__(self,name,color,age,sex)
        self.hair="短毛"
    def catch_rat(self):
        print("捉老鼠")
    def shout(self):
        print("喵喵叫")
