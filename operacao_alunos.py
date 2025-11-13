
# importando modulos
from funcoes import verificar_vazio, turma_list , alunos_list
from cadastros import cadastro_aluno

# função menu aluno
def menu_aluno():
    print("\n----------GERENCIAR ALUNO----------")
    print("\n1-Cadastrar Aluno")
    print("2-Listar Alunos")
    print("3-Buscar Aluno")
    print("4-Excluir Aluno")

# função para verificar se a turma existe
def percorrer_lista_turma():
    if verificar_vazio(turma_list,"turma"):
        print("Cadastre uma turma primeiro para poder cadastrar alunos\n")
        return False
    return True

# função que cadastra aluno
def cadastrar_aluno_opcao():
    aluno_novo = cadastro_aluno()
    if verificar_vazio(turma_list,"turma"):
        return
    alunos_list.append(aluno_novo)
    print(f"\nCadastro do aluno(a) {aluno_novo.nome} feito com sucesso ✅!!")
    print(f"RA do Aluno(a) {aluno_novo.nome} é : {aluno_novo.id}\n")

# função para listar todos alunos cadastrados
def listar_alunos_opcao():
    if verificar_vazio(alunos_list,"aluno"):
        return 
    print("\n----------Alunos Cadastrados no Sistema----------\n")
    alunos_list.print_list()

# função para buscar aluno
def buscar_aluno_opcao():
    if verificar_vazio(alunos_list , "aluno"):
        return
    buscar_aluno = str(input('\nDigite o RA do aluno que deseja buscar: ')).strip()
    for aluno in alunos_list.to_list():
        if aluno.id == buscar_aluno:
            print('\n------------ALUNO ENCONTRADO COM SUCESSO--------------\n')
            print(f'{aluno}\n')
            return
    print(f"\nO aluno {buscar_aluno} não foi encontrado no sistema\n")

# função para excluir aluno
def excluir_aluno_opcao():
    if verificar_vazio(alunos_list , "aluno"):
        return
    buscar_aluno = str(input("\nDigite o nome do aluno que deseja excluir : ")).strip()
    for aluno in alunos_list.to_list():
        if aluno.nome == buscar_aluno:
            alunos_list.remove(aluno)
            print("\nAluno {} excluido com sucesso ✅!!\n".format(buscar_aluno))
            return
    print("\nO aluno {} não está cadastrado no sistema\n".format(buscar_aluno))
