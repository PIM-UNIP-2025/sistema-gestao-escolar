# biblioteca para pegar letras maisculas e minusculas e numeros
from string import ascii_letters , digits
# biblioteca para pegar valores aletorios
from random import choice

# declarando class aluno 
class Aluno:
    # atributos do aluno
    def __init__(self , nome , turma):
        self.nome = nome
        self.turma = turma
        self.id = self.gerar_id()
        
    # Metodo que quando chamado por print ou str retorna as informações do aluno
    def __str__(self) -> str:
        return f'Ra : {self.id} | Nome : {self.nome} | Turma : {self.turma}'
    
    # gera id do aluno
    def gerar_id(self) -> str:
        caracters = ascii_letters + digits
        ra = ''.join(choice(caracters) for i in range(7))
        return ra
