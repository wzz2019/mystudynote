#学习类的属性引用
class Person():
    name='noname'
    def get_name(self):
        return self.name  #类变量，用self修饰

#可直接操作类的属性
print('Person类的name属性值：'+Person.name)
#实例化一个类，给类的具体对象一个别名
p=Person()
print('实例p的name属性值：'+p.name)
print('调用实例p的get_name方法：'+p.get_name())
#可修改实例类的属性，不影响类的属性
p.name='newname'
print('修改实例p的name属性后，实例p的name属性值：'+p.name)
print('修改实例p的name属性后，Person类的name属性值：'+Person.name)
#一旦实例化的类，如果修改类的属性，不影响实例对象的属性
Person.name='updatename'
print('修改Person类的属性后，Person类的name属性值：'+Person.name)
print('修改Person类的属性后，实例p的name属性值：'+p.name)