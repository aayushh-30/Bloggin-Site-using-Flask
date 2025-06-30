from flask import Flask,render_template
from db import engine, Base
from routes.post_Routes import post_bp
from routes.userRoutes import user_bp

app = Flask(__name__)

#Blueprint registration
app.register_blueprint(post_bp)
app.register_blueprint(user_bp)

# Table get Created if not exist 
Base.metadata.create_all(bind=engine)

#Test Routes
@app.route("/")
def Home():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)