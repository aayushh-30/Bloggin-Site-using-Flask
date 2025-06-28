from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.fun import list_posts,get_post

post_bp = Blueprint('posts', __name__, url_prefix='/posts')


@post_bp.route('/', methods=['GET'])
def show_posts():
    return list_posts(True)

@post_bp.route('/<int:id>',methods = ['GET'])
def find_post(id):
    post =  get_post(id)
    if post is None:
        return f"Not available"
    return post
