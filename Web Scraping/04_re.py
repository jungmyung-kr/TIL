import re

# ca?e 
# caae, cabe, cace, ....

p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미 > care, cave, case, cafe (O) / caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) / fade (X)
# $ (se$) : 문자열의 끝 > case, base, vase (O) / face (X)

def print_match(m):
    if m:
        print("m.group():",m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력 받은 문자열 (함수가 아닌 문자열이기 때문에 괄호 X)
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

m = p.match("careless")
print_match(m)
'''
match
: 주어진 문자열의 처음부터 일치하는지 확인 
따라서 careless의 경우 일치, 결과 반환
good care 불일치, '매칭되지 않음' 반환

m.group(): care
m.string: careless
m.start(): 0
m.end(): 4
m.span(): (0, 4)
'''

m = p.search("good care") 
print_match(m)
'''
search
: 주어진 문자열 중에 일치하는게 있는지 확인
따라서 이 경우에는 careless뿐만 아니라 good care도 일치 
'''

lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)
# ['care', 'cafe']

'''
간단 정리

1. p = re.compile("원하는 형태")
2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인 
4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 '리스트' 형태로 반환

원하는 형태 : 정규식
. (ca.e): 하나의 문자를 의미 > care, cave, case, cafe (O) / caffe (X)
^ (^de) : 문자열의 시작 > desk, destination (O) / fade (X)
$ (se$) : 문자열의 끝 > case, base, vase (O) / face (X) 
'''