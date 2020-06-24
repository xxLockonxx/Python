"""
    날짜 : 2020/06/24
    이름 : 이성진
    내용 : 모듈 교재 p207
"""

import Ch05.sub1.Calc as calc

# 모듈(파이썬 패키지에 있는 소스파일) 함수 호출
rs1 = calc.plus(1, 2)
rs2 = calc.minus(1, 2)
rs3 = calc.multi(2, 3)
rs4 = calc.div(4, 2)

print('rs1 :', rs1)
print('rs2 :', rs2)
print('rs3 :', rs3)
print('rs4 :', rs4)