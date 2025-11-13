# linked list
# declarando no
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

# declarando linked list de alunos
class ListaAlunos:
    def __init__(self):
        # cabeça
        self.head = None
        # tamanho da lista
        self.size = 0
    
    # metodo para adicionar aluno na lista
    def append(self , Object_aluno):
        # verifica se a cabeça é vazia , se a cabeça não for none(vazia) entra no if
        if self.head:
            # pointer recebe a cabeça
            pointer = self.head
            # percorre ate o ultimo elemento(até achar NEXT = none)
            while pointer.next:
                # atualiza o ponteiro
                pointer = pointer.next
            # adiciona o novo objeto em ultimo
            pointer.next = Node(Object_aluno)
            # incrementa 1 no tamanho(aumenta o tamanho da lista)
            self.size += 1
        else:
            # se a cabeça for vazia a cabeça recebe o novo objeto
            self.head = Node(Object_aluno)
            # incrementa 1 no tamanho(aumenta o tamanho da lista)
            self.size += 1
    
    # metodo para imprimir objetos
    def print_list(self):
        # pointer recebe primeiro elemento
        pointer = self.head
        # enquanto o valor for diferente de none
        while pointer:
            # imprimi valor
            print(f"{pointer.data}\n")
            # atualiza o ponteiro
            pointer = pointer.next
    
    # metodo que retorna o tamanho da lista de forma pythonica
    def __len__(self):
        return self.size
    
    # metodo que remove aluno da lista
    def remove(self, aluno):
        # se o aluno for o primeiro
        if aluno == self.head.data:
            # o primeiro aluno será o segundo
            self.head = self.head.next
            # decrementa 1 (diminui o tamanho da lista)
            self.size -= 1
            return

        # ponterio recebe o primeiro elemento
        pointer = self.head
        # previous recebe o valor anterior
        previous = None
        # percorre até for diferente de none
        while pointer:
            # se o valor for igual a aluno
            if pointer.data == aluno:
                # o anterior aponta para o proximo do valor a ser "excluido"
                previous.next = pointer.next
                # decrementa 1 (diminui o tamanho da lista)
                self.size -= 1
                return
            # se não atualiza o ponteiro atual e anterior
            previous = pointer
            pointer = pointer.next

    # metodo para adicionar valores numa lista
    def to_list(self):
        lista_alunos = []
        pointer = self.head
        while pointer:
            lista_alunos.append(pointer.data)
            pointer = pointer.next
        return lista_alunos
