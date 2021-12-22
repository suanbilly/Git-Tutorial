#SW Expert Academy

#2047. 신문 헤드라인
#final answer
T = "The_headline_is_the_text_indicating_the_nature_of_the_article_below_it."
texts=T.upper()
print(texts)

#2050. 알파벳을 숫자로 변환
#first
T='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph = {'A':'1', 'B':'2', 'C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9',\
        'J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17',\
        'R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
num = ''
for i in range(len(T)):
    for key, val in alph.items():
        if T[i] == key and len(T)-1 != i:
            num += val + ' '
        elif T[i] == key and len(T)-1 == i:
            num += val
        else:
            pass
print(num)

#final answer
T='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in T:
    print(ord(i) - 64, end = ' ')