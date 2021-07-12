import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests

# Response 상태 코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code)
print(r.ok) # status_code가 200이면 true를, 아니면 false를 반환한다
# 분기문을 사용해서 서버의 상태가 정상일 때만 정보를 받아오는 코드를 작성하는데 사용한다

# https://jsonplaceholder.typicode.com
# Json 데이터을 파싱할 때 테스트하기 유용한 사이트
r = s.get('https://jsonplaceholder.typicode.com/albums')
#print(r.text) # Array 형식으로 가져온다

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
# print(r.text) # JsonData 하나를 가져온다.
print(r.json()) # Json 형식으로 변환해준다. (Requests 모듈에서 제공해주는 기능)
print(r.json().keys()) # Dic 형식으로 키값만 가져온다.
print(r.json().values()) # Dic 형식으로 Values값만 가져온다
print(r.encoding) # response된 데이터의 인코딩을 알려준다
print(r.content) # 바이너리 형식으로 가져온다
print(r.raw) # raw 데이터 형식으로 가져온다
