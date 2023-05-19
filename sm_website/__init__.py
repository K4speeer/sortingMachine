from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ADD_A_SECRET_KEY_BEFORE_DEPLOYING'


    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app 