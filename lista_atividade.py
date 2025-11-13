# declara no
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

# declara linkedlist lista atividades
class ListaAtividade:
    def __init__(self):
        # cabeça
        self.head = None
        # tamanho da lista
        self.size = 0
    
    # metodo para adicionar atividade
    def append(self , Object_atividade):
        # se a cabeça não for none entra no if 
        if self.head:
            # define ponteiro
            pointer = self.head
            # equanto não for none (percorre ate o ultimo no)
            while pointer.next:
                # atualiza ponteiro
                pointer = pointer.next
            # adiciona objeto em ultimo
            pointer.next = Node(Object_atividade)
            # incrementa 1 na lista (aumenta o tamanho da lista)
            self.size += 1
        else:
            # se a lista for vazia(cabeça == none) adiciona novo no em head
            self.head = Node(Object_atividade)
            # incrementa 1 na lista (aumenta o tamanho da lista)
            self.size += 1
        
    # metodo para imprimir objetos
    def print_list(self):
        # ponteiro recebe o primeiro valor da lista
        pointer = self.head
        # enquanto não for none 
        while pointer:
            # printa o objeto
            print(f"{pointer.data}\n")
            # atualiza o ponteiro
            pointer = pointer.next
    
    # metodo len para definir o tamanho da lista em forma pythonica
    def __len__(self):
        return self.size
    
    # metodo para remove objeto da lista
    def remove(self, atividade):
        # se o a atividade a ser excluida for a primeira  
        if atividade == self.head.data:
            # a cabeça recebe o segundo objeto
            self.head = self.head.next
            # decrementa 1 (diminui o tamanho da lista)
            self.size -= 1
            return

        # ponteiro aponta para primeiro elemento da lista    
        pointer = self.head
        # ponteiro que aponta para o elemento anterior da lista
        previous = None
        # enquanto o ponteiro não for none
        while pointer:
            # se o elemnto for igual a atividade
            if pointer.data == atividade:
                # elemento anterior do elemento escolhido aponta para o proximo elemento do elemento escolhido
                previous.next = pointer.next
                # decrementa 1 (diminui o tamanho da lista)
                self.size -= 1
                return
            
            # atualiza ponteiros
            previous = pointer
            pointer = pointer.next

    # metodo para adicionar elemento em uma lista
    def to_list(self):
        lista_atividade = []
        pointer = self.head
        while pointer:
            lista_atividade.append(pointer.data)
            pointer = pointer.next
        return lista_atividade
