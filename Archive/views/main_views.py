import sqlite3
import pandas as pd
from datetime import datetime
from flask import Blueprint, render_template, g

bp = Blueprint('main', __name__, url_prefix='/')

def get_db():
    return sqlite3.connect('./archive.db')

def get_posts_from_db():
    posts = []
    cursor = g.db.cursor()
    cursor.execute('SELECT * FROM post')
    rows = cursor.fetchall()
    # rows=g.db.execute('select a.id, a.title, b.username, a.post_dated, a.content from post as a join user as b on a.author_id == b.id')
    # print(rows)
    for row in rows:
        print(f'test id: {row[0]}')
        print(f'test author: {row[2]}')
        print(f'test title: {row[1]}')
        print(f'test date_posted: {row[3]}')
        print(f'test: {row[4]}')
        article = {
            'id': row[0],
            'author': {
                'username': row[2]
            },
            'title': row[1],
            'content': row[4],
            'date_posted': datetime.strptime(row[3], '%Y-%m-%d')
        }
        # print(article)
        posts.append(article)
    return posts

@bp.before_request
def before_request():
    g.db = get_db()
    print('db connected')

@bp.teardown_request
def teardown_request(exeption):
    g.db.close()
    print('db closed')

@bp.route('/')
@bp.route('/index')
def index():
    posts = get_posts_from_db()
    return render_template('index.html', posts=posts)

@bp.route('/')
@bp.route('/article/<int:article_id>')
def article(article_id):
    posts = get_posts_from_db()
    # print(posts)
    post = None
    for row in posts:
        if row['id'] == article_id:
            post = row
            # return render_template('content.html', post=post)
            break
    return render_template('article.html', post=post)

@bp.route('/about')
def about():
    return render_template('about.html', title='About')


