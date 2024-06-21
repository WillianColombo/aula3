from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)


"""

ROTAS PARA CLIENTES

    - /clientes/    (GET) Listar os clientes
    - /clientes/    (POST) Inserir um cliente no servidor
    - /clientes/new    (GET) Renderizar um formulário para criar um cliente
    - /cliente<id>     (GET) Obter os dados de um cliente   
    - /cliente<id>/edit     (GET) Renderizar um formulário para editar um cliente
    - /cliente<id>/update   (PUT) Atualizar os dados de um cliente
    - /cliente<id>/delete   (DELETE) Deleta o registro do usuário    

"""
    
@cliente_route.route('/')
def lista_clientes():
    clientes = Cliente.select()
    return render_template("lista_clientes.html", clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    
    data = request.json
    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )
    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    return render_template("formulario_cliente.html")

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    return render_template("detalhe_cliente.html", cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    return render_template("formulario_cliente.html", cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    cliente_editado = Cliente.get_by_id(cliente_id)
    data = request.json
    
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
    
    return render_template('item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}