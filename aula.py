# Declarando class aula
class Aula:
    # atributos de aula
    def __init__(self , data , turma , tema):
        self.data = data
        self.turma = turma
        self.tema = tema
    
    # Metodo que quando chamado por print ou str retorna as informações da aula
    def __str__(self) -> str:
       return f'Data da Aula : {self.data} | Turma : {self.turma} | Tema da Aula : {self.tema}'
