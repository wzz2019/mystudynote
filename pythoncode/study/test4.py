#类的属性作用域
class person():
    name=''
    age=0
    __weight=0      #__可以定义私有变量，无法直接通过修改实例属性的方式修改，可以通过初始化修改
    __height=0
    def __init__(self,n,a,h): #定义构造方法，可以通过参数实例化类的属性
        self.name=n
        self.age=a
        self.__height=h
    def set_weight(self,w):     #定义方法，可以修改私有变量
        self.__weight=w
    def get_age(self):
        print("%s%d岁了"%(self.name,self.age))
    def get_weight(self):
        print("%s体重%d"%(self.name,self.__weight))
    def get_height(self):
        print("%s身高%d"%(self.name,self.__height))

#实例化类
p=person('小明',10,100)
# print(dir(p))
p.get_age()

p.__weight=80
p.__height=80
p.get_weight()
p.get_height()
p.set_weight(80)
p.get_weight()
