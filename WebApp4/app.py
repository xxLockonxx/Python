"""
    날짜 : 2020/06/25
    이름 : 이성진
    내용 : 파이썬 웹 프로그래밍 데이터 베이스
"""
from flask import Flask, render_template, redirect
from WebApp4.views.register import register_blueprint
from WebApp4.views.list import list_blueprint

app = Flask(__name__)

app.register_blueprint(register_blueprint)
app.register_blueprint(list_blueprint)

@app.route('/')
def index():
    return redirect('/register')

if __name__=='__main__':
    app.run()