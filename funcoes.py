# biblioteca que manipula o sistema operacional
from os import system
# modulo lista de alunos
from lista_alunos import ListaAlunos
# modulo lista de aulas
from lista_aula import ListaAulas
# modulo lista de atividades
from lista_atividade import ListaAtividade
# modulo lista de turmas
from lista_turma import ListaTurma

# função que limpa a tela
def limpar_tela():
    cmd = 'cls'
    return system(cmd)

# função que verifica se o usurio deseja continuar
def continuar():
    op = str(input("Deseja voltar para o menu principal ? :  [S/N]")).lower().strip()
    if op == 'n':
        return op == 'n'

# função que verifica se uma lista esta vazia
def verificar_vazio(lista,tipo):
    if len(lista) == 0:
        print(f"\nLista de {tipo}s vazia\n")
        return True
    return False

# função de input
def ler_texto():
    opcao = str(input("\nDigite umas das opçoes acima: ")).strip()
    return opcao

# lista de alunos
alunos_list = ListaAlunos()
# lista das turmas
turma_list  = ListaTurma()
# lista de aulas
aula_list   = ListaAulas()
# lista de atividades
atividade_list = ListaAtividade()
