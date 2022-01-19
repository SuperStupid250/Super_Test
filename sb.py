import requests, json
from selenium import webdriver
import requests, csv
import time


#url = "https://api.sync-sign.com/v2/user/monitor?type=online&deviceType=NODE&nodeId={}".format(i)
#url = "https://api.sync-sign.com/v2/user/monitor?type=online&deviceType=NODE&nodeId={{nodeId}}"


nodelist = ['00124b0023acfaa8','00124b0023acf799','00124b0023acf568','00124b0023acfaab','00124b0023acf7b8','00124b0023acfd4c','00124b0023acfd13','00124b0023ad32e5','00124b0023acf7d8','00124b0023acfd50','00124b0023acfab1','00124b0023acf7bf','00124b0023acf54c','00124b0023acf7e8','00124b0023acf576','00124b0023acf55a','00124b0023acf540','00124b0023acfaf1','00124b0023acfab7','00124b0023acfd3f','00124b0023acf55f','00124b0023acf543','00124b0023acf7e0','00124b0023acfabb','00124b0023acf7ae','00124b0023acfd3d','00124b0023acfac2','00124b0023acfd2b']
#nodelist = ['00124b0023acfaa8']
payload={}
for i in nodelist:
  url = "https://api.sync-sign.com/v2/user/monitor?type=online&deviceType=NODE&nodeId={}".format(i)
  headers = {
    'Authorization': 'Bearer a4fb5a1cf0cd8eee987eaf0d7803dc8e75a7196f'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  a = response.text
  driver = webdriver.Chrome()
  driver.get(eval(a)["data"]["signUrl"])
  time.sleep(5)

  f = csv.reader(open('C:/Users/Administrator/Downloads/{}.csv'.format(i), 'r'))
  num = 0
  for i in f:
    if i[3][6:8] >= '14':
      if i[4] == 'false':
        num += 1
    else:
      continue

  print(str(i[1])+": "+str(num))
  f = open('C:/Users/Administrator/Desktop/0119.csv', mode='a+', encoding='utf-8')
  csv_writer = csv.writer(f)
  csv_writer.writerow([str(i[1]), num])



























