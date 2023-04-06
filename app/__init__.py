from flask import Flask

def create_app():
    app =  Flask(__name__)
    
     
    # Configuración de la aplicación
    app.config['SECRET_KEY'] = 'mi_clave_secreta'
    
    # Importar y registrar blueprints
    from .views import bp
    app.register_blueprint(bp)
    
    
    return app