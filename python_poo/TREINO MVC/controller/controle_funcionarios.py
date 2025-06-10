from model.funcionario import funcionario
from model.funcionario_dao import funcionarioDAO

class controle_funcionarios:
    def __init__(self):
        self.dao = funcionarioDAO()
    
    def inserir(self,nome,cargo,salario):
        funcionanario = funcionario(nome,cargo,salario)
        self.dao.inserir(funcionanario)
        return print("funcionario cadastrado")
    
    def lista(self):
        self.dao.listar_todos()