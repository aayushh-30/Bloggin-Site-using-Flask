from flask import Flask
from db import engine, Base
from routes.post_Routes import post_bp

app = Flask(__name__)

app.register_blueprint(post_bp)
Base.metadata.create_all(bind=engine)

@app.route("/")
def Home():
    return f"Home Page"

if __name__ == "__main__":
    app.run(debug=True)