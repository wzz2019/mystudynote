import yaml

with open("./data_cal.yml") as f:
    list=yaml.safe_load(f)
    print(list)
    print(list["sub"])
    # addlist=yaml.safe_load(f)["add"]
    # sublist=yaml.safe_load(f)["sub"]
    # mullist=yaml.safe_load(f)["mul"]
    # divlist=yaml.safe_load(f)["div"]
    #
    # print(addlist)
    # print(sublist)
    # print(mullist)
    # print(divlist)