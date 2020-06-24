"""
    날짜 : 2020/06/24
    이름 : 이성진
    내용 : 파이썬 데이터베이스 프로그래밍 SELECT
"""

import pymysql as db

# 데이터베이스 접속
conn = db.connect(host='192.168.44.46',
                  user='lsj',
                  password='1234',
                  db='lsj',
                  charset='utf8')
# 쿼리문 실행객체 생성
cur = conn.cursor()

# 쿼리문 실행
cur.execute("SELECT * FROM `USER1`")

for row in cur.fetchall():
    print('-------------------------')
    print('아이디 :', row[0])
    print('이  름 :', row[1])
    print('휴대폰 :', row[2])
    print('나  이 :', row[3])
    print('-------------------------')

# 데이터베이스 종료
conn.close()
