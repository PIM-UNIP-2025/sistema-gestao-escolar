# declara no
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

# declara linkedlist turma
class ListaTurma:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # metodo para adicionar um elemento no final da lista
    def append(self , Object_turma):
        # se a cabeça não for vazia entra no if
        if self.head:
            # ponteiro que aponta para o primeiro valor
            pointer = self.head
            # enquanto não for none
            while pointer.next:
                # atualiza ponteiro
                pointer = pointer.next
            # adiciona um novo no em ultimo na lista
            pointer.next = Node(Object_turma)
            # incrementa 1(aumenta o tamanho da lista)
            self.size += 1
        else:
            # senão cabeça(primeiro) recebe o novo no
            self.head = Node(Object_turma)
            # incrementa 1(aumenta o tamanho da lista)
            self.size += 1
    
    # metodo para imprimir elementos da lista
    def print_list(self):
        pointer = self.head
        while pointer:
            print(f"{pointer.data}\n")
            pointer = pointer.next
    
    # metodo da definir tamanho da lista de forma pythonica
    def __len__(self):
        return self.size
    
    # metodo para remove um elemento da lista
    def remove(self, turma):
        # se a turma escolhida for a primeira
        if turma == self.head.data:
            # cabeça(primeiro no) recebe o segundo elemento
            self.head = self.head.next
            # decrementa 1(diminui o tamanho da lista)
            self.size -= 1    
        
        # ponteiro aponta para o primeiro elemento
        pointer = self.head
        # ponteiro que aponta para o anterior
        previous = None
        # enquanto não for none
        while pointer:
            # se o elemento for igual a turma
            if pointer.data == turma:
                # o elemento anterior da turma escolhida aponta para a proxima elemento da turma escolhida 
                previous.next = pointer.next
                # diminui o tamanho da lista
                self.size -= 1
                return
            
            # atualiza os ponteiros 
            previous = pointer
            pointer = pointer.next

    # metodo que adciona os elemento em uma lista    
    def to_list(self):
        lista_turma_geral = []
        pointer = self.head
        while pointer:
            lista_turma_geral.append(pointer.data)
            pointer = pointer.next
        return lista_turma_geral
