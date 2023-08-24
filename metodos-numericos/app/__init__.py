from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuraciones
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

    # Inicialización de extensiones (si estás usando alguna)

    # Importa rutas y registra blueprints
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
