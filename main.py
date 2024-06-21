from flask import Flask
from configuration import configurar_tudo

# Inicialização
app = Flask(__name__)

# Script que configura as rotas e o banco de dados
configurar_tudo(app)        

# Execução
app.run(debug=True)