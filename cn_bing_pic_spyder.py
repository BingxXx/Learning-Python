import requests
import re
import time

today = time.strftime("%Y.%m.%d")

url = 'http://cn.bing.com'
conn = requests.get(url)
content = conn.text
print(content)
reg = r"https://cn.bing.com/az/hprichbg/rb/.*?.jpg)"
pattern = re.compile(reg,re.S)
# a_herf = re.findall(reg,content,re.S)[0]
a_herf = pattern.match(content)[0]
print(a_herf)
today_picture = requests.get(a_herf)
f = open('%s.jpg' % today, 'wb')
f.write(today_picture.content)
f.close()


# https://cn.bing.com/az/hprichbg/rb/ZhangjiajieLandscape_ZH-CN13434455714_1920x1080.jpg
