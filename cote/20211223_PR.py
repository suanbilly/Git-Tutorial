# 프로그래머스
# 정수 제곱근 판별
#1
def solution(n):
    a = n ** 0.5
    if int(a) == a:
        return (n ** 0.5 + 1) ** 2
    else:
        return -1

solution(121)
solution(3)
#2
import math
def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return (math.sqrt(n)+1) ** 2
    else:
        return -1

solution(121)
solution(3)

# 이상한 문자 만들기
def solution(s):
    texts = s.split(" ") #공백 표시해줘야 함..
    result = []
    for i in texts:
        text = ''
        for j in range(len(i)):
            if j%2 == 0:
                text += i[j].upper()
            else:
                text += i[j].lower()
        result.append(text)
    return ' '.join(result)

solution("try hello world")