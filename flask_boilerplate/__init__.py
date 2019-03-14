from flask import Flask

from flask import Flask, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return 'This is a flask-boilerplate project, not to be used in production.'

    @app.route('/hello')
    def hello():
        name = request.args.get('name', 'World')
        return f'Hello {name}!'

    return app
