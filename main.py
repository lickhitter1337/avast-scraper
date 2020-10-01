import requests
import json

query = input("EMail > ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://www.avast.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.avast.com/',
}

data = {
    'email':query
}

try:
    response = requests.post('https://digibody.avast.com/v1/web/leaks', headers=headers, json=data)
    jsondata = json.loads(response.text)
    leakamount = len(jsondata['value'])
    for i in range(leakamount):
        print(query + " | " +  jsondata['value'][i]['username'] + " | " + jsondata['value'][i]['leak_info']['title'])
except:
    print("No leaks were found :(")
