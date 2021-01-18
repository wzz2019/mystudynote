import json
# initjsondata=json.load(open("list.json"))["data"]
# list_T=[]
# for jsondata in initjsondata:
#   page_title=jsondata["data"]["page_title"]
#   list=jsondata["data"]["components"]
#   for item in list:
#     if item["type"]=="goods":
#       level=item["title"]
#       list2=item["list"]
#       for item2 in list2:
#         itemlist={}
#         title=item2["title"]
#         src_id=item2["src_id"]
#         jump_url=item2["jump_url"]
#         itemlist["page_title"]=page_title
#         itemlist["level"]=level
#         itemlist["title"]=title
#         itemlist["jump_url"]=jump_url
#         list_T.append(itemlist)
#         print("%s=%s=%s=%s" % (itemlist["page_title"], itemlist["level"], itemlist["title"], itemlist["jump_url"]))



initjsondata=json.load(open("list2.json"))["data"]
for jsondata in initjsondata:
  list=jsondata["data"]["contentData"]["contentInfo"]
  for item in list:
    title=item["title"]
    resourceId=item["availableInfo"]["resourceId"]
    productId=item["availableInfo"]["productId"]
    # print(title)
    print("https://wxe04072521886a147.h5.xiaoe-tech.com/v1/course/video/"+resourceId+"?pro_id="+productId)
