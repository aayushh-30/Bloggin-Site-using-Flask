from flask import Blueprint, request,url_for,redirect,render_template
from controllers.fun import delete_Post, list_posts,get_post,update_post,create_post

#Blueprint creation for folder structure, regd to app.py
post_bp = Blueprint('posts', __name__, url_prefix='/posts')

#1st argument is important for redirection, all the routes in this page can be accessed as "posts.name_of_function"
#Same for other blueprints as well


@post_bp.route('/', methods=['GET'])
def show_posts():
    posts = list_posts(True)
    return render_template('base.html',allPosts = posts)
@post_bp.route('/<int:id>',methods = ['GET'])
def find_post(id):
    post =  get_post(id)
    if post is None:
        return f"Not available"
    return [post.title,post.body]

@post_bp.route('/update/<int:id>',methods = ['PUT'])
def Post_Updation(id):
    form_data = request.form.to_dict()
    update_post(id,form_data)
    return redirect(url_for('posts.show_posts'))

@post_bp.route('/create', methods=['GET','POST'])
def post_creation():
    if request.method == 'GET':
        return render_template('createPost.html')
    form_data = request.form
    result = create_post(form_data)
    return result

# @post_bp.route('/delete/<int:id>',methods = ['DELETE'])
# def delete_post(id):
#     status,status_code = delete_Post(id)
#     if status_code == 200:
#         return {{url_for('posts.show_posts')}}
    
#     return {{}}

    


