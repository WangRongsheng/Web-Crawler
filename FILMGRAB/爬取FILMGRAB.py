import requests
import re

url = "https://film-grab.com/"
page = requests.get(url).text
# print(page)
res = re.compile(r'src="(http.+?.jpg)"')
reg = re.findall(res,page)
#print(reg)
num = 1
for i in reg:
    a = requests.get(i)
    f = open(str(num)+".jpg","wb")
    f.write(a.content)
    f.close
    print("第%s张图片下载成功！"%num)
    num = num + 1
