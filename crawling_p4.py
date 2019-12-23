import os
import sys
import urllib.request
import json
from matplotlib import pyplot as plt
from ast import literal_eval

client_id = "[client_id]"
client_secret = "[client_secret]"
url = "https://openapi.naver.com/v1/datalab/search";
#body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"삼성\",\"keywords\":[\"한글\",\"korean\"]},{\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
#
# body_dict = {"startDate": "2017-01-01",
#                 "endDate": "2017-04-30",
#              "timeUnit": "month",
#              "keywordGroups": [{"groupName":"삼성",
#                                 "keywords": ["삼성","Samsung"]}]}

body_dict = {
    "startDate":"2019-01-01",
    "endDate":"2019-04-30",
    "timeUnit":"date",
    "keywordGroups":[
        {"groupName":"타다","keywords":["타다","소카","vcnc","VCNC"]},
    ],
}

body = json.dumps(body_dict)
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    scraped = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)


print(scraped)
dictionary = literal_eval(scraped)

ratio = [each['ratio'] for each in dictionary['results'][0]['data']]
date = [each['period'] for each in dictionary['results'][0]['data']]

plt.figure(figsize=(18,6))
plt.plot(date, ratio)
plt.grid()
plt.xticks(rotation=90)
plt.show()