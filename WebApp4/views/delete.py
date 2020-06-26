from flask import Blueprint, render_template, request
import pymysql as db

list_blueprint = Blueprint('list', __name__)

@list_blueprint.route('/list')
def delete():

    # 데이터베이스 접속
    conn = db.connect(host='192.168.44.46',
                      user='lsj',
                      password='1234',
                      db='lsj',
                      charset='utf8')

    # 쿼리문 실행 객체 생성
    cur = conn.cursor()

    # 쿼리문 실행
    sql = cur.execute("DELETE * FROM `USER3` WHERE  `uid`=?")
    cur.execute(sql)
    conn.commit()

    # 데이터베이스 종료
    conn.close()


    return render_template('/list.html')