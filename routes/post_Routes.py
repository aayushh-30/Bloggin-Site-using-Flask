from flask import Blueprint, render_template, request, redirect, url_for, flash

post_bp = Blueprint('posts', __name__, url_prefix='/posts')


@post_bp.route('/', methods=['GET'])
def show_posts():
    pass
