from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
@index_blueprint.route('/index')
def index():
    return render_template('/register.html')