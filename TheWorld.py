import time
import csv
def RecordingTime(func):

    def inner(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print('本轮刷新时间：'+str(end-start)+' 秒')

    return inner



def TheLog(nodeid,e):
    a = open('C:/Users/Administrator/Desktop/123.txt', mode='a+', encoding='utf-8')
    a.write('设备' + str(nodeid) + '在' + str(time.asctime( time.localtime(time.time()) )) + '出现问题： ' + str(e) + '\n')
    # f = open('C:/Users/Administrator/Desktop/123.csv', mode='a+', encoding='utf-8')
    # csv_writer = csv.writer(f)
    # csv_writer.writerow([nodeid,e])


