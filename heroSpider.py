import requests
import urllib
import json
import os
import threading

 #读取英雄信息，关键是数字名称
with open('E:\\python\\herolist.json','r',encoding='utf-8') as f:
    jsonFile=json.load(f)

def download_picture():

    #批量提取数据
    for m in range(len(jsonFile)):#动态计算所有英雄个数
        #数字名称
        eName=jsonFile[m]['ename']
        #中文名称
        cName=jsonFile[m]['cname']
        #所有皮肤名称
        skinName=jsonFile[m]['skin_name'].split('|')
        #计算皮肤个数
        skinNumbers=len(skinName)

        #print(eName,cName,skinName)

        #下载皮肤
        for n in range(1,skinNumbers+1):
            #构造图片信息
            pictureUrl='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(eName)+'/'+str(eName)+'-bigskin-{}.jpg'.format(n)

            #下载图片:content表示以二进制格式表示
            picture=requests.request('get',pictureUrl).content
            #requests.get(pictureUrl)
            #保存图片,图片是二进制
            #with open('E:\\python\\Reuslt\\Pictures\\'+cName+skinName[n-1]+'.jpg','wb') as ff:
                #ff.write(picture)
            #写入文件：方式二
            path='E:\\python\\Reuslt\\Test\\'+cName+'\\'
            isExists=os.path.exists(path)
            if not isExists:
                os.makedirs(path)
                print('创建目录成功!')
            else:
                print('目录已经存在')
            urllib.request.urlretrieve(pictureUrl,'E:\\python\\Reuslt\\Test\\'+cName+'\\'+skinName[n-1]+'.jpg')

