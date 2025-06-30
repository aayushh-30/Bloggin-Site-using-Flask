from db import engine,Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models.user import User

def createUser(form_data,methods = ['POST']):
    # id = form_data["id"]
    email = form_data["email"]
    username = form_data["username"]
    password = form_data["password"]

    if id is None or email is None or username is None or password is None:
        return f"All credentials are required"

    try:
        session = Session()
        user = User(username = username,password = password)
        user.email = email
        session.add(user)
        session.commit()
        return "User created Successfully !!"
    except SQLAlchemyError as e:
        session.rollback()
        return str(e)
    finally:
        session.close()

def loginUser(form_data, methods=['POST']):
    print("Form Data:", form_data)  # DEBUG
    email = form_data.get("email")
    password = form_data.get("password")

    print("Email:", email)  # DEBUG
    print("Password:", password)  # DEBUG

    if not email or not password:
        return "All fields are required"

    session = Session()
    try:
        user = session.query(User).filter(User._email == email).first()
        print("User fetched:", user)  # DEBUG

        if user is None:
            return "User does not exist"

        if user.password == password:
            return "Login successful"
        else:
            return "Incorrect password"

    except SQLAlchemyError as e:
        session.rollback()
        return f"Database error: {str(e)}"

    finally:
        session.close()
