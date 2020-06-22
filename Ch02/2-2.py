"""
    날짜 : 2020/06/22
    이름 : 이성진
    내용 : 문자열 자료형 실습하기 교재 p44
"""
# 문자열 더하기
str1 = 'Hello\t'
str2 = 'Python!'
str3 = str1 + str2
print('str3 : ', str3)

# 문자열 곱하기
str = 'python!'
print('str * 5 : ', str*5)

# 문자열 길이
hello = 'Hello World'
print('hello 길이 : ', len(hello))

# 문자열 인덱스
print('hello[0]: ', hello[0])
print('hello[6]: ', hello[6])

# 문자열 슬사이스
print('hello[0:7] : ', hello[0:7])
print('hello[1:7] : ', hello[1:7])
print('hello[:7] : ', hello[:7])
print('hello[7:] : ', hello[7:])
print('hello[-1] : ', hello[-1])
print('hello[-2] : ', hello[-2])

# 문자열 분리
animal = '사자,호랑이,코끼리,기린'
a1, a2, a3, a4 = animal.split(',')

print('a1 :', a1)
print('a2 :', a2)
print('a3 :', a3)
print('a4 :', a4)

# 문자열 포맷
fm1 = '오늘은 %d월 입니다.'
fm2 = '오늘은 %d월 %d일 입니다.'
fm3 = '오늘은 %s월 입니다.'
fm4 = '오늘은 %s년 %d월 %d일 %s요일 입니다.'

print(fm1 % 6)
print(fm2 % (6, 22))
print(fm3 % '06')
print(fm4 % ('2020', 6, 22, '월'))

# 문자열 관련 함수 교재 p67 ~ 71

# 문자 개수 세기(count)
a = "hobby"
count = a.count('b')
print('count :', count)

# 위치 알려주기 1(find)
a = "Python is the best choice"
findb = a.find('b')
print('findb: ', findb)
findk = a.find('k')
print('findk: ', findk)

# 위치 알려주기 2(index)

a = "Life is too short"
indext = a.index('t')
print('indext :', indext)
#indexk = a.index('k')
#print('indexk :', indexk) k가 없어서 오류발생


# 문자열 삽입(join)
joinabcd = ",".join('abcd')
print('joinabcd :', joinabcd)

joinabc = ",".join(['a', 'b', 'c', 'd'])
print('a,b,c,d : ', joinabc)