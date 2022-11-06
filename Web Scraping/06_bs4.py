import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = req uests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


##############################################

print(soup.title) # <title>네이버 웹툰 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text()) # 네이버 웹툰 > 요일별  웹툰 > 전체웹툰

##############################################

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

##############################################

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# class 속성이 Nbtn_upload인 a element 찾는 코드
# <a class="Nbtn_upload" href="/mypage/myActivity" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>

print(soup.find(attrs={"class":"Nbtn_upload"}))
# class 속성이 Nbtn_upload인 어떤 element 찾는 코드 (div, a, ...)
# <a class="Nbtn_upload" href="/mypage/myActivity" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>

##############################################

print(soup.find("li", attrs={"class":"rank01"}))
'''
<li class="rank01">
<a href="/webtoon/detail?titleId=736277&amp;no=156" onclick="nclk_v2(event,'rnk*p.cont','736277','1')" title="싸움독학-152화 : 밥은 잘 주나요?">싸움독학-152화 : 밥은 잘 주나요?</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
'''

# 위처럼 긴 태그가 아니라 딱 a 태그 부분만 보고 싶다면?
# 변수에 저장한 후, 해당 객체 내 필요 태그부분만 호출, 출력
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)

print(rank1.a.get_text())
# 싸움독학-152화 : 밥은 잘 주나요?

##############################################


print(rank1.next_sibling)
# 출력 사항 없음. 태그 사이에 개행(줄바꿈)이 있어서 그럴 수도 있음 : 빈 줄 출력
print(rank1.next_sibling.next_sibling)
'''
<li class="rank02">
<a href="/webtoon/detail?titleId=795262&amp;no=24" onclick="nclk_v2(event,'rnk*p.cont','795262','2')" title="사형소년-24화_가족">사형소년-24화_가족</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
'''

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

print(rank1.parent)
'''
<ol class="asideBoxRank" id="realTimeRankFavorite">
<li class="rank01">
<a href="/webtoon/detail?titleId=736277&amp;no=156" onclick="nclk_v2(event,'rnk*p.cont','736277','1')" title="싸움독학-152화 : 밥은 잘 주나요?">싸움독학-152화 : 밥은 잘 주나요?</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
<li class="rank02">
<a href="/webtoon/detail?titleId=795262&amp;no=24" onclick="nclk_v2(event,'rnk*p.cont','795262','2')" title="사형소년-24화_가족">사형소년-24화_가족</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
<li class="rank03">
<a href="/webtoon/detail?titleId=758150&amp;no=105" onclick="nclk_v2(event,'rnk*p.cont','758150','3')" title="입학용병-104화">입학용병-104화</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
<li class="rank04">
<a href="/webtoon/detail?titleId=710751&amp;no=216" onclick="nclk_v2(event,'rnk*p.cont','710751','4')" title="약한영웅-215화">약한영웅-215화</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
<li class="rank05">
<a href="/webtoon/detail?titleId=785251&amp;no=50" onclick="nclk_v2(event,'rnk*p.cont','785251','5')" title="시월드가 내게 집착한다-49화">시월드가 내게 집착한다-49화</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
<li class="rank06">
<a href="/webtoon/detail?titleId=798664&amp;no=11" onclick="nclk_v2(event,'rnk*p.cont','798664','6')" title="자매전쟁-11 진짜는 누구 (3) ">자매전쟁-11 진짜는 누구 (3)</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
<li class="rank07">
<a href="/webtoon/detail?titleId=761104&amp;no=103" onclick="nclk_v2(event,'rnk*p.cont','761104','7')" title="곱게 키웠더니, 짐승-외전 10화">곱게 키웠더니, 짐승-외전 10화</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
<li class="rank08">
<a href="/webtoon/detail?titleId=783524&amp;no=37" onclick="nclk_v2(event,'rnk*p.cont','783524','8')" title="고백 취소도 되나?-36화">고백 취소도 되나?-36화</a>
<span class="rankBox">
<img alt="순위상승" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_up.gif" title="순위상승" width="7"/>1



                                </span>
</li>
<li class="rank09">
<a href="/webtoon/detail?titleId=774831&amp;no=71" onclick="nclk_v2(event,'rnk*p.cont','774831','9')" title="수희0(tngmlek0)-71화">수희0(tngmlek0)-71화</a>
<span class="rankBox">
<img alt="순위하락" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_down.gif" title="순위하락" width="7"/>1




                                </span>
</li>
<li class="rank10">
<a href="/webtoon/detail?titleId=799805&amp;no=11" onclick="nclk_v2(event,'rnk*p.cont','799805','10')" title="분신으로 자동사냥-11화 우장산 이글아이 (1)">분신으로 자동사냥-11화 우장산 이글아이 (1)</a>
<span class="rankBox">
<img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


                                </span>
</li>
</ol>
'''

##############################################

rank2 = rank1.find_next_sibling()
# 개행이 있을 수 도 있기 때문에 보다 간단하게 실질적인 sibling만 찾는것
print(rank2.a.get_text())

rank3 = rank2.find_next_sibling()
print(rank3.a.get_text())

rank2 = rank3.find_previous_sibling()
print(rank2.a.get_text())

##############################################

print(rank1.find_next_siblings("li"))
# rank1의 형제들을 가져옴 

##############################################

webtoon = soup.find("a", text = "사형소년-24화_가족")
print(webtoon)
# <a href="/webtoon/detail?titleId=795262&amp;no=24" onclick="nclk_v2(event,'rnk*p.cont','795262','2')" title="사형소년-24화_가족">사형소년-24화_가족</a>
