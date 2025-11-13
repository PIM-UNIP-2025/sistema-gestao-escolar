# declarando class turma
class Turma:
    # atributos de turma
    def __init__(self , nome , semestre , curso):
        self.nome = nome
        self.semestre = semestre
        self.curso = curso
        
    # metodo para imprimir todas as informções da turma(atravez da função print ou str)
    def __str__(self) -> str:
        return f'Turma : {self.nome} | Semestre :  {self.semestre} | Curso : {self.curso}'
