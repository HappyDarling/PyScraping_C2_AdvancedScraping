import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests, json

s = requests.Session()

# Json 데이터가 Stream형태일 경우
r = s.get('http://httpbin.org/stream/20')
# print(r.text)
# print(r.json()) # Stream 형식으로 이루어져있기 때문에 json으로 불러올 수 없음
# print(r.encoding)

if r.encoding is None: # 예외를 바로잡는 코딩
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True): # 응답 데이터를 한 번에 한 줄 반복하면서 대용량 응답을 위해 콘텐츠를 한 번에 메모리로 읽는 것을 방지
    # print(line)
    # print(json.loads(line))
    b = json.loads(line) # 각 한 줄들을 Json 데이터로 변환해주는 코드, json 모듈에 속한다
    print(b['url']) # url을 키로 하는 values의 값을 출력해준다
    print(type(b)) # Dictionary형태라고 나오는 것을 알 수 있다.


r = s.get('http://httpbin.org/stream/20', stream=True) # Stream을 명시해주는 것이 좋음

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    b = json.loads(line) # dict
    for e in b.keys(): # key값만 빼내어주는 함수
        print("key:", e, ", value:", b[e])
