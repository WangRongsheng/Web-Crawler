## 爬虫反爬措施

1. 加入随机等待时间
2. 加入随机`UserAgent`
```python
from fake_useragent import UserAgent

headers = {
            'authority': 'www.pixiv.net',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': UserAgent(verify_ssl=False).random,   # 随机生成
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'xxxxx', 
        }
```
3. 代理ip池

## 参考

1. [用爬虫批量下载P站图片](https://www.bilibili.com/video/BV1Hy4y1m7Kf)
2. [不能上P站也能把图片批量爬虫到本地！ 手把手教你自建免费代理ip池！](https://www.bilibili.com/video/BV1xt4y1673q)