import requests,json,time


for i in range(0,50):
    url = 'https://weclub.ccc.cmbchina.com/SCRMActivity/new-point/request/draw-lottery.json'
    headers={"Content-type":"application/json;charset=UTF-8",
             "Cookie":"xAgentAID=110a7430-176ebed3903a-2def12cabf634a7aa53d54bbae696966; accessToken=f81bd75ff5ff071ceef590947d99868abb4f6758726b3a304fc87a58bc68f69e; xAgentUID=lzqSIEyO1C4LtB%2BOULoUxThacKjs9EmyjLb081jyat8%3D"
             }
    body={"activityCode":"POI0000038","subId":1189}
    r = requests.post(url=url,data=json.dumps(body), headers=headers,verify=False)
    print(r.text)
    time.sleep(5)

