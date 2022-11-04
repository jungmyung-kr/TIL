import requests

res = requests.get("http://google.com")
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("mygoogle.html","w", encoding="utf8") as f:
    # mygoogle.html이라는 파일명, 쓰기모드, 인코딩 방식 지정
    f.write(res.text)