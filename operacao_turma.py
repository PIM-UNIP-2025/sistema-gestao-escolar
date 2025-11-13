# importando modulos
from cadastros import cadastro_turma
from funcoes import turma_list , verificar_vazio , alunos_list

# função para cadastrar turma
def cadastrar_turma_opcao():
    turma_nova = cadastro_turma()
    for turma in turma_list.to_list():
        if turma.nome == turma_nova.nome:
            print("\nNão pode haver Turmas com nomes iguais\1!!\n")
            return
    turma_list.append(turma_nova)
    print("\nTurma Cadastrada com Sucesso ✅!!\n")

# função para listar turmas
def listar_turmas_opcao():
    if verificar_vazio(turma_list,"turma"):
        return
    print("\n---------Turmas Cadastradas no Sistema------------\n")
    turma_list.print_list()

# função para buscar turma
def buscar_turma_opcao():
    if verificar_vazio(turma_list,"turma"):
        return
    buscar_turma = str(input("\nDigite o nome da Turma: ")).strip()
    found = False
    print(f"\n----------ALUNOS NA TURMA {buscar_turma}----------\n")
    for aluno in alunos_list.to_list():
        if aluno.turma == buscar_turma:
            print(f"-{aluno.nome}\n")
            found = True
    if not found:
        print("Não há alunos cadastrados no sistema\n")

# função para excluir turma
def excluir_turma_opcao():
    if verificar_vazio(turma_list,"turma"):
        return
    
    print("\n----------Excluindo Turma----------\n")
    buscar_turma = str(input("\nDigite o nome da turma que deseja excluir: ")).strip()

    turma_encontrada = None

    for turma in turma_list.to_list():
        if turma.nome == buscar_turma:
            turma_encontrada = turma
            break
    
    if not turma_encontrada:
        print(f"\nA turma {buscar_turma} não foi encontrada!\n")
        return
    
    turma_list.remove(turma_encontrada)
    print(f"\nTurma {buscar_turma} excluida com sucesso!\n")

    
    for aluno in alunos_list.to_list():
        if aluno.turma == buscar_turma:
            aluno.turma = None
            print(f"Aluno {aluno.nome} sem turma")

    print("\nOperação concluida com sucesso\n")            
