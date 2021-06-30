import socket
import json
import requests
from requests import get
from urllib import request
import datetime
'''
    获取城市的备用方法（不准确，可能在国外准确）
    reader = geoip2.database.Reader('/path/to/GeoLite2-City.mmdb')
    response = reader.city('223.104.204.27')
    print(response.city)
'''

# get_inner_ip函数用于获取局域网ip，
# 参考自 https://blog.csdn.net/u013314786/article/details/78962103


def get_inner_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

# get_outer_ip函数用于获取公网ip，
# 参考自 https://www.codegrepper.com/code-examples/python/python+get+public+ip+address


def get_outer_ip():
    ip = get('https://api.ipify.org').text
    return ip

# get_ip_location函数用于通过ip获取位置，使用了百度的api,
# 参考自 https://blog.csdn.net/fugitive1/article/details/82500299


def get_ip_location(ip):
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

# get_weather函数用于通过位置查询天气，
# 参考自 https://zacksock.blog.csdn.net/article/details/102580920


def get_weather(city):
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
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    url = 'http://www.autmone.com/openapi/icalendar/queryDate?date='+str(now_time)
    lunar = requests.get(url)
    lunar = lunar.json()
    # 下面两个数值先用不着,留着以后可能有用
    # chimonth = lunar["data"]["iMonthChinese"]
    # chiday = lunar["data"]["iDayChinese"]
    month = lunar["data"]["sMonth"]
    cyear = lunar["data"]["cYear"]
    cmonth = lunar["data"]["cMonth"]
    cday = lunar["data"]["cDay"]
    return cyear, cmonth, cday, month


def run_main():
    inner_ip = get_inner_ip()
    outer_ip = get_outer_ip()
    ip_location = get_ip_location(outer_ip)
    weather = get_weather(ip_location[2])
    lunar = get_lunar()
    return inner_ip, outer_ip, ip_location, weather, lunar
