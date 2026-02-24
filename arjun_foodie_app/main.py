from flask import Flask
from .config import Config
from .database_ext import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .foodie_routes import api_bp

    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True,port=5001)

#to run :  python -m arjun_foodie_app.main