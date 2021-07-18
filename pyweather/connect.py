import socket
import json
import os
import requests
from requests import get
from urllib import request
import datetime
import pickle
import geoip2.database
from PyQt5.QtWidgets import QMessageBox


def get_inner_ip():
    """
    get_inner_ip函数用于获取局域网ip，
    参考自 https://blog.csdn.net/u013314786/article/details/78962103
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_outer_ip1():
    """
    get_outer_ip函数用于获取公网ip，
    参考自 https://www.codegrepper.com/code-examples/python/python+get+public+ip+address
    """
    ip = get('https://api.ipify.org').text
    return ip


def get_outer_ip2():
    ip = requests.get('http://ip-api.com/json/?lang=zh-CN')
    ip = ip.json()
    ip = ip['query']
    return ip


def get_ip_location(ip):
    """
    get_ip_location函数用于通过ip获取位置，使用了百度的api,
    参考自 https://blog.csdn.net/fugitive1/article/details/82500299
    """
    baidu_api_ak = 'nuA6qd7lXWRyfYOnTVYdhrO8WEHeaGhh'
    url = "http://api.map.baidu.com/location/ip?ak=" + baidu_api_ak + "&ip=" + ip
    req = request.Request(url)
    res = request.urlopen(req)
    res = res.read()
    n = res.decode(encoding='utf-8')
    s = json.loads(n)
    address = s['address']
    address = address.split('|')
    country = address[0]
    province = address[1]
    city = address[2]
    return country, province, city


def get_weather(city):
    """
    get_weather函数用于通过位置查询天气，
    参考自 https://zacksock.blog.csdn.net/article/details/102580920
    """
    weather_url = "http://wthrcdn.etouch.cn/weather_mini?city="
    data = weather_url + city
    weather_res = requests.get(data)
    d = weather_res.json()
    date = (d["data"]["forecast"][0]["date"])
    high = (d["data"]["forecast"][0]["high"])
    low = (d["data"]["forecast"][0]["low"])
    wind = (d["data"]["forecast"][0]["fengxiang"])
    speed = (d["data"]["forecast"][0]["fengli"])
    # 下面的replace为了去掉 <![CDATA[]]>
    speed = speed.replace('<![CDATA[', '')
    speed = speed.replace(']]>', '')
    wind = wind + speed
    weather_type = (d["data"]["forecast"][0]["type"])
    return date, high, low, weather_type, wind


def get_lunar():
    """
    get_lunar函数用于获取农历信息
    api参考自 https://blog.csdn.net/nbskycity/article/details/106554894
    """
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')  # 把时间按api要求格式化
    url = 'http://www.autmone.com/openapi/icalendar/queryDate?date='+str(now_time)
    lunar = requests.get(url)
    lunar = lunar.json()
    chimonth = lunar["data"]["iMonthChinese"]
    chiday = lunar["data"]["iDayChinese"]
    month = lunar["data"]["sMonth"]
    cyear = lunar["data"]["cYear"]
    return cyear, chimonth, chiday, month


def run_main():
    try:
        inner_ip = get_inner_ip()
        outer_ip = get_outer_ip2()
        ip_location = get_ip_location(outer_ip)
        weather = get_weather(ip_location[2])
        lunar = get_lunar()
        return [inner_ip, outer_ip, ip_location, weather, lunar]
    except:
        try:
            inner_ip = None
            outer_ip = get_outer_ip2()
            ip_location = foreign(outer_ip)
            weather = ('', '', '', '', '')
            lunar = ('', '', '', '')
            return [inner_ip, outer_ip, ip_location, weather, lunar]
        except:
            QMessageBox.critical(None, '网络异常', '网络未响应，请检查网络', QMessageBox.Ok)


def save_history(info):
    """
    save_history把每次打开窗口获取的信息存储到history.pkl中
    """
    try:
        f = open('history.pkl', 'rb')
        content = pickle.load(f)
        f.close()
        save_time = datetime.datetime.now()
        save_time = str(save_time).split(".")[0]
        content[save_time] = info
        with open('history.pkl', 'wb') as f:
            pickle.dump(content, f)
    except FileNotFoundError:
        f = open('history.pkl', 'wb')
        pickle.dump({}, f)
        f.close()
        save_history(info)
    except EOFError:
        f = open('history.pkl', 'wb')
        pickle.dump({}, f)
        f.close()
        save_history(info)
    except TypeError:
        f = open('history.pkl', 'wb')
        pickle.dump({}, f)
        f.close()
        save_history(info)
    else:
        pass


def foreign(ip):
    path = os.path.abspath('.')
    reader = geoip2.database.Reader(path + '/GeoLite2-City.mmdb')
    response = reader.city(ip)
    city = response.city.name
    province = response.continent.name
    country = response.country.name
    return country, province, city
