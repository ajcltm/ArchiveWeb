from datetime import datetime
from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

posts = [
    {
        'author': {
            'username':'kim'
        },
        'title': 'The first post',
        'content': 'This is the first post contents',
        'date_posted': datetime.strptime('2021-8-25', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'kim'
        },
        'title': 'The second post',
        'content': 'This is the second post contents',
        'date_posted': datetime.strptime('2021-8-25', '%Y-%m-%d')
    }
]
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', posts=posts)

@bp.route('/about')
def about():
    return render_template('about.html', title='About')


