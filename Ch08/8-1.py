"""
    날짜 : 2020/06/24
    이름 : 이성진
    내용 : 파이썬 데이터베이스 프로그래밍
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
cur.execute("INSERT INTO `USER1` VALUES ('P101','김유신','010-1111-1111', 23)")

# 쿼리문 실행 확정
conn.commit()

# 데이터베이스 종료
conn.close()

print('INSERT 완료...')