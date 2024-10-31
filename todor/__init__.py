from flask import Flask, render_template, url_for

def create_app():
    app = Flask(__name__)

    # configurando el proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev' # esta clave es solo para pruebas
    )

    # Registrar Blueprint del modulo todo
    from . import todo
    app.register_blueprint(todo.bp)

    # Registrar Blueprint del modulo auth - lo que equivale a las vistas de este archivo
    from . import auth
    app.register_blueprint(auth.bp)
     
    @app.route('/')
    def index():
        return render_template('index.html') 
    
    @app.route('/registrar')
    def registrar():
        return render_template('registrar.html')

    return app