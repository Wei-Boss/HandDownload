import os
import socket
import urllib.error
import datetime
import time
from urllib.request import urlopen
from urllib.request import urlretrieve


socket.setdefaulttimeout(5)
wilte_list = ['12345678']
#白名单学号
img_url = 'www.baidu.com'
#网页地址


def start_megumi():
    start_time = time.time()
    for period in range(15, 19):
    #period 届区间(15届至18届)
        for code in range(1, 26):
        #code 学院代码区间
            path = str(period) + '/' + str(code).rjust(2, '0')
            os.makedirs(path, exist_ok=True)
            send('===%s 文件夹创建成功!===' % path)
            for i in range(0, 900):
            #i 学号区间
                id = str(period) + str(code).rjust(2, '0') + str(i).rjust(4, '0')
                if id in wilte_list:
                    continue
                urllib_download(id, path)
    end_time = time.time()
    send('已完成! 用时 %s 分钟' % int((end_time - start_time) / 60))


def urllib_download(id, path):
    url = img_url + str(id) + '.jpg'
    file = path + '/' + str(id) + '.jpg'
    if os.path.exists(file):
        send('学号 %s 已存在!' % str(id))
        return
    try:
        urlopen(url)
        urlretrieve(url, file)
        send('学号 %s 下载成功!' % str(id))
    except urllib.error.URLError:
        send('学号 %s 不存在!' % str(id))
        return
    


def send(msg):
    time = datetime.datetime.now().strftime('%H:%M:%S')
    print('[%s][Megumi] %s' % (time, msg))


start_megumi()