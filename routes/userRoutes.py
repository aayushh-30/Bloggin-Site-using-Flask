from flask import Blueprint, request,url_for,redirect,render_template
from controllers.userControllers import loginUser,createUser
from controllers.fun import getAllPostOfUser
user_bp = Blueprint('users', __name__, url_prefix='/user')

@user_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('loginForm.html')
    form_data = request.form
    status,username,stCode = loginUser(form_data)
    if stCode == 200 :
        allPosts,stCode = getAllPostOfUser(id)
        if stCode == 200:
            return render_template("profile.html",userCred = username, allPosts = allPosts )
        else:
            return f"Something Went wrong"
    else:
        return render_template("loginForm.html")
    
@user_bp.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signUpform.html')
    form_data = request.form
    status = createUser(form_data)
    return render_template("loginForm.html")

