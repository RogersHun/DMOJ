"""
Tmoj - ccc18j1

Q.
네자리 전화번호 중 다음 세 조건 모두 충족하면 텔레마케터의 전화번호임
1. 첫 번째 숫자는 8또는 9임
2. 네 번째 숫자는 8또는 9임
3. 두 번째와 세 번째 숫자는 동일함
텔레마케터 번호면 ignore, 아니면 answer을 출력
"""
import random

a = random.randint(1000,9999)
a = str(a)
if a[0] == 8 or 9 and a[3] == 8 or 9 and a[1] == a[2]:
    print(a)
    print('ignore')
else : 
    print(a)
    print('Call')