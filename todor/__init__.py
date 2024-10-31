from flask import Flask

app = Flask(__name__)


# primera ruta
@app.route('/')
def index():
    return 'Hello World'
