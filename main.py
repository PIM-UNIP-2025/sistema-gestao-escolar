# importando modulos
from funcoes import ler_texto , limpar_tela , continuar
from menus import * 

# função menu
def sistema_academico():

    # carrega os dados salvos
    carregar_dados()
    

    while True:
        # limpa a tela do usuario
        limpar_tela()
        # imprimi menu principal
        menu_principal()
        
        # dicionario com todas as opções
        opcoes = {
            '1' : menu_principal_aluno,
            '2' : menu_principal_turma,
            '3' : menu_aula_principal,
            '4' : menu_principal_atividade,
            '5' : menu_princiapal_ia,
            '6' : menu_principal_relatorio,
            '7' : encerrar
        }

        # usuario recebe input
        opcao = ler_texto()
        # variavel recebe opção escolhida pelo usuario
        funcao = opcoes.get(opcao)
        # se != none
        if funcao:
            # opção escolhida pelo usuario
            funcao()
            # se a opção for 7 salva os dados e encerra o programa 
            if opcao == '7':
                salvar_dados()
                break
            # executa função para decidir se o usuario deseja continuar no programa
            if continuar():
                print("\nPROGRAMA ENCERRADO\n")
                salvar_dados()
                break
        # tratamento caso o usuario digite uma opção errada
        else:
            print("\nDigite um valor válido\n")


if __name__ == "__main__":
    sistema_academico()
