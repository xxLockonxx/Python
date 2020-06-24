"""
    날짜 : 2020/06/24
    이름 : 이성진
    내용 : 내장함수 교재 p231
"""
# abs() : 절대값
r1 = abs(-5)
r2 = abs(5)
print('r1 :', r1)
print('r2 :', r2)

# all() : 리스트에서 0이 포함됐는지 검사하는 함수
r3 = all([1,2,3,4,5])
r4 = all([1,2,3,4,0])

print('r3 :', r3)
print('r4 :', r4)

# any() : 리스트에서 하나라도 True 값이 있으면 전체 True, 모두 False 이면 전체 False
r5 = any([0, '', None, False, 5]) # 2-7에서 확인할 수 있음.
r6 = any([0, '', None, False, []]) # 모두 false 인 경우

print('r5 :', r5)
print('r6 :', r6)
    
# enumerate() : 반복문에서 인덱스값과 원소갑을 동시에 출력
people = ['김유신', '김춘추', '장보고']

for i, name in enumerate(people):
    print(i, name)

# lambda() :
def sum(a, b):
    return a+b
add = lambda a,b:a+b

r7 = sum(1, 2)
r8 = add(1, 2)

print('r7 :', r7)
print('r8 :', r8)