import requests,json,time


for i in range(0,50):
    url = 'https://weclub.ccc.cmbchina.com/SCRMActivity/new-point/request/draw-lottery.json'
    headers={"Content-type":"application/json;charset=UTF-8",
             "Cookie":"xAgentAID=110a7430-176ebed3903a-2def12cabf634a7aa53d54bbae696966; accessToken=92ffc2905ce2a9cbe0be4016bf238cfac1d6076054472713e4e2bb9209d156fd; xAgentUID=lzqSIEyO1C4LtB%2BOULoUxThacKjs9EmyjLb081jyat8%3D"
             }
    body={"activityCode":"POI0000038","subId":1189}
    r = requests.post(url=url,data=json.dumps(body), headers=headers,verify=False)
    print(r.text)
    time.sleep(5)

