from flask import Flask
from models.post import Post
from models.tag import Tag
from models.user import User

app = Flask(__name__)

@app.route("/")
def Home():
    return f"Home Page"

if __name__ == "__main__":
    app.run(debug=True)