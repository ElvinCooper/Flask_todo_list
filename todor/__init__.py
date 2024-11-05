#import sqlalchemy
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)

    # configurando el proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev' ,# esta clave es solo para pruebas
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    )


    # inicializar la conexion con la base de datos
    db.init_app(app)


    # Registrar Blueprint del modulo todo
    from . import todo
    app.register_blueprint(todo.bp)

    # Registrar Blueprint del modulo auth - lo que equivale a las vistas de este archivo
    from . import auth
    app.register_blueprint(auth.bp)
     
    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        db.create_all()


    return app