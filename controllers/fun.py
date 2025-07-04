from db import engine,Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models.post import Post

Session = sessionmaker(bind=engine)


def get_post(post_id):
    session = Session()
    try:
        post = session.query(Post).get(post_id)
        return post
    except SQLAlchemyError as e:
        session.rollback()
        return e
    finally:
        session.close()

def list_posts(published):
    session = Session()
    try:
        posts = session.query(Post).filter(Post.is_published == published).all()
        return posts
    except SQLAlchemyError as e:
        session.rollback()
        return e
    finally:
        session.close()

def create_post(form):
    session = Session()
    try:
        post = Post(
                    title = form["title"],
                    body = form["body"],
                    is_published = form["is_published"] in ['true', 'True', True, 1],
                    )
        session.add(post)
        session.commit()
        return "Posted"
    except SQLAlchemyError as e:
        session.rollback()
        return str(e)
    finally:
        session.close()

def update_post(post_id, form):
    session = Session()
    try:
        post = session.get(Post, post_id)
        if not post:
            return "Invalid Post ID"

        title = form.get("title")
        body = form.get("body")
        is_published = form.get("is_published")

        # Validate fields if you're enforcing required fields
        if title is not None and title.strip() == "":
            return "Title cannot be empty"
        if body is not None and body.strip() == "":
            return "Body cannot be empty"

        # Update only provided fields
        if title is not None:
            post.title = title
        if body is not None:
            post.body = body
        if is_published is not None:
            post.is_published = is_published in ["true", "True", "1", 1, True]

        session.commit()
        return "Post updated successfully"
    
    except SQLAlchemyError as e:
        session.rollback()
        return f"Database Error: {str(e)}"
    
    finally:
        session.close()

def list_drafts():
    posts = list_posts(published=False)
    return posts

def delete_Post(post_id):
    session = Session()
    try:
        post = session.query(Post).get(post_id)
        if not post:
            return f"Post with id {post_id} not found.",401

        session.delete(post)
        session.commit()
        return f"Post with id {post_id} deleted successfully.",200
    except SQLAlchemyError as e:
        session.rollback()
        return e
    finally:
        session.close()

def getAllPostOfUser(user_id):
    session = Session()
    try:
        posts = session.query(Post).filter(Post.user_id == user_id).all()
        if not posts:
            return f"No posts found for user with id {user_id}.", 404

        return posts, 200
    except SQLAlchemyError as e:
        session.rollback()
        return str(e), 500
    finally:
        session.close()
