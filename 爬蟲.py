#讓網頁認為是正常訪問
import urllib.request as req
url = 'https://poe.ninja/challenge/cluster-jewels'

#建立一個request物件，附加 request headers的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)

#解析原始碼

import bs4
root = bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")#尋找class_="title"的div標籤
for title in titles:
    if title.a != None: #印出標題含有A 標籤
        print(title.a.astring)
        
print(titles)