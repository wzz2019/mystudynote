"""
写一个Bycycle（自行车）类，有run（骑行）方法，输入里程数，显示人工骑行里程数
写一个EBycycle(电动车)方法继承Bycycle，自有属性电量
每骑行10公里耗电1度，计算最大自动骑行里程数
重写run,输入里程数，根据电量显示需要人工骑行里程数
"""
class Bycycle():
    def run(self,km):
        print(f"人工骑行里程数(km)：{km}")
class EBycycle(Bycycle):
    def __init__(self,battery):
        self.battery=battery
        self.max_mile = self.battery * 10
        print(f"电量：{self.battery}，需要骑行{self.max_mile}km")
    def autorun(self):
        print(f"自动骑行里程数(km)：{self.max_mile}")
    def run(self,km):
        if km> self.max_mile:
            self.autorun()
            #调用父类被覆盖的方法
            super().run(km-self.max_mile)
        else:
            print(f"自动骑行里程数(km)：{km}")
if __name__=="__main__":
    eb=EBycycle(20)
    eb.run(300)

    import yaml

    with open("bycycle.yml") as f:
        datas=yaml.safe_load(f)

    # print(datas)
    eb=EBycycle(datas["default"]["battery"])
    eb.run(datas["default"]["km"])

    f.close()