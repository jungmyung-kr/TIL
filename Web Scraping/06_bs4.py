import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title) # <title>네이버 웹툰 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text()) # 네이버 웹툰 > 요일별  웹툰 > 전체웹툰

print(soup.a) # soup 객체 내 첫번째로 발견되는 a라는 element의 정보를 요구

print(soup.a.attrs) # a element의 속성 정보 출력
# attrs (attributes : 속성)
'''
{'href': '#menu', 
'onclick': "document.getElementById('menu').tabIndex=-1;
document.getElementById('menu').focus();
return false;"}
'''
print(soup.a["href"]) # a element의 href 속성 '값' 출력
# #menu