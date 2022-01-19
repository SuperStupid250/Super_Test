import requests, json
from selenium import webdriver  #导入第三方包
import requests, csv            #导入第三方包
import time                     #导入第三方包


#url = "https://api.sync-sign.com/v2/user/monitor?type=online&deviceType=NODE&nodeId={}".format(i)
#url = "https://api.sync-sign.com/v2/user/monitor?type=online&deviceType=NODE&nodeId={{nodeId}}"

#导入nodeid
nodelist = ['00124b0023acfaa8','00124b0023acf799','00124b0023acf568','00124b0023acfaab','00124b0023acf7b8','00124b0023acfd4c','00124b0023acfd13','00124b0023ad32e5','00124b0023acf7d8','00124b0023acfd50','00124b0023acfab1','00124b0023acf7bf','00124b0023acf54c','00124b0023acf7e8','00124b0023acf576','00124b0023acf55a','00124b0023acf540','00124b0023acfaf1','00124b0023acfab7','00124b0023acfd3f','00124b0023acf55f','00124b0023acf543','00124b0023acf7e0','00124b0023acfabb','00124b0023acf7ae','00124b0023acfd3d','00124b0023acfac2','00124b0023acfd2b']
#nodelist = ['00124b0023acfaa8']
payload={} #json在python相当于字典 创建个字典储存payload
for i in nodelist:    #用i分别充当nodelist里面的每一项
  #设置好接口url
  url = "https://api.sync-sign.com/v2/user/monitor?type=online&deviceType=NODE&nodeId={}".format(i)
  #设置好请求头  ：里面带token访问
  headers = {
    'Authorization': 'Bearer cb983195f5fe40a9b9eea8a40c0d8101a858b7ad'
  }
  response = requests.request("GET", url, headers=headers, data=payload) #发get请求给服务器
  a = response.text  #把请求得到的结果转成 text格式
  driver = webdriver.Chrome()   #自动打开谷歌浏览器
  driver.get(eval(a)["data"]["signUrl"])    #谷歌浏览器访问请求里面get结果得到的url
  time.sleep(5)       #浏览器需要反应时间 这里设置5秒给他下载

  f = csv.reader(open('C:/Users/Administrator/Downloads/{}.csv'.format(i), 'r')) #打开csv，文件名为当前循环到的nodeid
  num = 0  #初始化false出现的次数
  for i in f:     #用i 遍历csv读出来的每一行
    if i[3][0:2] == '22':   #如果年份=22 进入下一层判断
      if i[3][3:5] == '01':  #如果月份=11  进入下一层判断
        if i[3][6:8] >= '18':  #如果日期>=18  进入下一层判断

          if i[4] == 'false':  #如果在线状态为false 执行一下语句
            num += 1       #num自加1
          else:        #否则
            continue   #提前结束此次循环 进入下次循环(下一个nodeid)

  print(str(i[1])+": "+str(num))     #打印 nodeid + false出现的次数
  f = open('C:/Users/Administrator/Desktop/0119.csv', mode='a+', encoding='utf-8') #打开csv
  csv_writer = csv.writer(f)       #进入写模式
  csv_writer.writerow([str(i[1]), num])  #把本次结果写进去



























