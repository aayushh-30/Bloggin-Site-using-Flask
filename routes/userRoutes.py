from flask import Blueprint, request,url_for,redirect,render_template
from controllers.userControllers import loginUser,createUser
user_bp = Blueprint('users', __name__, url_prefix='/user')

@user_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('loginForm.html')
    form_data = request.form
    status = loginUser(form_data)
    return status
    
@user_bp.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signUpform.html')
    form_data = request.form
    status = createUser(form_data)
    return status

