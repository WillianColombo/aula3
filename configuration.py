from database.models.cliente import Cliente
from database.database import db
from routes.home import home_route
from routes.cliente import cliente_route

def configurar_tudo(app):
    configurar_db()
    configurar_routes(app)

def configurar_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')

def configurar_db():
    db.connect()
    db.create_tables([Cliente])
