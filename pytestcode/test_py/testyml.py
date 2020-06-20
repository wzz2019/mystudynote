import yaml

a=yaml.safe_load(open("./data_cal_add.yml"))
print(type(a))
print(a)
print(a["add"][0])

print(yaml.dump(a))