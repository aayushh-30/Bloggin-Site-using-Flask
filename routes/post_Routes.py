from flask import Blueprint, request,url_for,redirect
from controllers.fun import list_posts,get_post,update_post,create_post


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

@post_bp.route('/update/<int:id>',methods = ['PUT'])
def Post_Updation(id):
    form_data = request.form.to_dict()
    update_post(id,form_data)
    return redirect(url_for('posts.show_posts'))

@post_bp.route('/create', methods=['POST'])
def post_creation():
    form_data = request.form.to_dict()
    result = create_post(form_data)
    return result


