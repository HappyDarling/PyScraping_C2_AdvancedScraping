import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests

s = requests.Session()

#r = s.get('https://naver.com') # PUT(FETCH), DELETE, GET, POST
#print('1', r.text) # Naver의 메인페이지를 반환하여 Get 방식으로 가져온다

r = s.get('http://httpbin.org/cookies', cookies={'from' : 'myName'})
# Http Response를 테스트할 수 있는 사이트
# cookies라는 변수를 활용해서 Dictionary 형식으로 요청
print(r.text)

# header를 요청하는 구문
url = 'http://httpbin.org/get'
headers = {'User-Agent' : 'myPythonApp_1.0.0'}
r = s.get(url, headers=headers)
print(r.text)

s.close()

# with문을 사용한 requests
with requests.Session() as s:
    r = s.get('https://www.naver.com')
    #print(r.text)
