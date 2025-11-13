# declarando class atividade
class Atividade:
    # atributos da atividade
    def __init__(self , nome , data , turma):
        self.nome = nome 
        self.data = data
        self.turma = turma
    
    # Metodo que quando chamado por print ou str retorna as informações da atividade
    def __str__(self) -> str:
        return f'Nome da Atividade : {self.nome} | Data da Atividade : {self.data} | Turma : {self.turma}'
