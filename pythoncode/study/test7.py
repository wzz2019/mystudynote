# f=open('testfile')
# print(f.read())
# f.close()
#
# with open('testfile') as f:
#     print(f.read())
"""学习json的转换与读写"""
import json
info=[{
			"code": "SH600887",
			"name": "伊利股份",
			"value": 2127.0
		}, {
			"code": "SZ000725",
			"name": "京东方A",
			"value": 1961.0
		}]
"""dumps：将json转换成字符串格式"""
data=json.dumps(info,indent=2)
print(data)
print(type(data))
"""dump：将json转换成字符串，并存在文件里"""
data=json.dump(info,open('testfile','w'),indent=2)
"""loads：将字符串转换成json"""
info='''
[{
			"code": "SH600887",
			"name": "伊利股份",
			"value": 2127.0
		}, {
			"code": "SZ000725",
			"name": "京东方A",
			"value": 1961.0
		}]
'''
js=json.loads(info)
print(js)
print(type(js))
"""load：读取将文件中的内容转换成json"""
js=json.load(open('testfile'))
print(js)
print(type(js))