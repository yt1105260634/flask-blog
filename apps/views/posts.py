from flask import Blueprint, render_template

_posts = Blueprint('posts',__name__)

@_posts.route('/posts/')
def posts():
    return '收藏'