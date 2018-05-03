import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_url(url):
    header = {
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "zh - CN, zh;q = 0.9",
        # "Cache - Control": "max - age = 0",
        "Connection": "keep - alive",
        "Cookie": "newstatisticUUID=1525314081_1353725534",
        "Host": "www.xs8.cn",
        "Referer": "https: // www.xs8.cn / all?catId = 30031",
        "Upgrade - Insecure - Requests": "1",
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181Safari / 537.36"
    }
    html = urllib.request.Request(url, headers=header, method='GET')
    html = urllib.request.urlopen(html)
    html = html.read().decode('utf-8')

    soup = BeautifulSoup(html, 'lxml')
    for i in soup.select('#j-catalogWrap > div.volume-wrap > div:nth-of-type(1) > ul > li > a '):
        urls="https://"+i['data-cid'].strip("//")
        print(urls+"正在下载中...................")
        html = urlopen(urls)
        soup = BeautifulSoup(html, 'lxml')
        for i in soup.find('div', {'class': 'read-content j_readContent'}).children:
            with open('D:\\python\\test\\read.txt', 'a+', encoding='GB18030') as f:  # 由于网页是utf-8,但是必须要以gbk写入，所以必须为GB18030
                f.writelines(i)
                f.write('\n')
url='https://www.xs8.cn/book/8957149604581603#Catalog'
print(get_url(url))

