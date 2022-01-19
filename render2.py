import requests
import json
import time
import datetime
import os
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from show_nodeid import SHOW_NODEID
#from templateCar import SHOW_NODEID
from TheWorld import *
import random
#from test import test_node_id


URL = "https://api.sync-sign.com/v2/key/"
NG_LIST = ['00124B0023ACF532', '00124b0002098a8b', '00124b0002098a56']


API_KEY = "ed21892b-c51f-4caf-9dc9-39b9360abb04"
HUB = 'MCF008D166A584'

#即将出货设备
# API_KEY = "b62d6002-a5a4-45e5-82f8-e1471027b51c"
# HUB = 'MC7C9EBD29182C'

INTERVAL = 60 # x秒刷一次
TIME_ZONE = 8 # 时区是8

class WEBAPI:
    #@RecordingTime
    def __init__(self,):
        self.start()

    # def pathGetSn(self):
    #     return URL+API_KEY+"/devices"

    # def pathGetRenderSta(self,render_id):
    #     return URL+API_KEY+"/renders/"+render_id

    def pathGetNodeId(self,HUB_SN): #url合成 获取与中心关联的所有节点
        return URL + API_KEY +"/devices/" + HUB_SN + "/nodes"

    def pathPostLayout(self,node_id):  # url合成
        return URL+API_KEY+"/nodes/"+node_id+"/renders"

    # GET BEIJIN TIME, RETURN STR
    def getBeijingTime(self):
        SHA_TZ = timezone(
            timedelta(hours=TIME_ZONE),
            name='Asia/Shanghai',
        )
        utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
        beijing_now = utc_now.astimezone(SHA_TZ)
        return beijing_now.strftime('%a, %b %d %H:%M')

    # GET NODE LIST IN HUB
    def getNodeIdList(self,HUB_SN):
        nodeIdList = []
        # 获取某个hub下的nodeId
        r = requests.get(self.pathGetNodeId(HUB_SN))
        r_text = json.loads(r.text)         #解码
        try:
            if r_text["code"] == 200:
                for nodeid in r_text["data"]:
                    nodeIdList.append(nodeid["nodeId"])
                return nodeIdList
            else:
                print (r_text["code"])
                return []
        except Exception as e:
            print('11111'+str(e))
            print(r_text)
            TheLog(HUB_SN,'获取hub下面的node时出错')


    def getLayout(self,layout):
        return json.loads(layout)

    # PUSH LAYOUT TO CLOUD
    def render(self,nodeId,l):
        try:
            r = requests.post(self.pathPostLayout(nodeId),json = l)
            r_text=json.loads(r.text)
            try:
                if r_text["code"] == 200:
                    # renderId = r_text["data"]["renderId"]
                    # print(r_text["data"]["renderId"])
                    print('nodeID :' + nodeId + "请求成功")
                else:
                    print(r_text["code"])
                    return None
            except Exception as e:
                print('2222222'+str(e))
                print("r_text: "+r_text)
                TheLog(nodeId,'疑似掉线')
                return None
        except Exception as e:
            print('33333'+str(e))
            TheLog(nodeId,'客户端提交模板失败/掉线')
            return None


    def start(self):
        i = 0
        while True:
            @RecordingTime
            def starttime():
                try:

                    nodeIdList = []
                    nodeIdList = self.getNodeIdList(HUB)
                    try:
                        # GET NODE LIST
                        nodeIdList = []
                        nodeIdList = self.getNodeIdList(HUB)
                        print("node count ",len(nodeIdList))
                        print(nodeIdList)

                        layout = self.getLayout(SHOW_NODEID)
                        for l in layout["layout"]["items"]:
                            if l["data"]["id"] == "SXCS":
                                l["data"]["text"] = str(i)#self.getBeijingTime()
                        # print(layout)
                        for l in layout["layout"]["items"]:
                            if l["data"]["id"] == "BEIJING_TIME":
                                l["data"]["text"] = self.getBeijingTime()

                        for l in layout["layout"]["items"]:
                            if l["data"]["id"] == "UPCOMING_1_SUMMARY":
                                l["data"]["text"] = 'eat' + random.choice(['Pig feet rice','McDonalds','XiaoYuHao','KeWeiYuan','Dumplings','Snail powder'])

                        # START TO PUSH LAYOUT FOR NODEID IN NODELIST
                        for nodeId in nodeIdList:
                            if nodeId in NG_LIST:
                                continue
                            self.render(nodeId,layout)


                    except Exception as e:
                        print('4444'+str(e))
                        for nodeId in nodeIdList:
                            TheLog(nodeId,e)

                except:
                    print('get nodelist error')


                print("sleep for ",INTERVAL,"s")
                time.sleep(INTERVAL)

            starttime()
            i += 1
            print('当前刷新次数为：'+str(i)+'次\n====================================================隔离线================================================================')

if __name__ == "__main__":
        WEBAPI()