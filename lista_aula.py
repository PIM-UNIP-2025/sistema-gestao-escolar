# declara no
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

# declara linkedlist de aulas
class ListaAulas:
    def __init__(self):
        # cabeça
        self.head = None
        # tamanho da lista
        self.size = 0
    
    # metodo para adicionar elemento em ultimo
    def append(self , Object_aula):
        # se a cabeça não for none entra no if
        if self.head:
            # ponteiro recebe primeiro valor da lista
            pointer = self.head
            # enquanto não for none
            while pointer.next:
                # atualiza ponteiro
                pointer = pointer.next
            # adicionar novo no em ultimo
            pointer.next = Node(Object_aula)
            # incrementa 1(aumenta o tamanho da lista)
            self.size += 1
        else:
            # senão o primeiro elemento recebe o novo no
            self.head = Node(Object_aula)
            # incrementa 1(aumenta o tamanho da lista)
            self.size += 1
    
    # metodo imprimi todos os elementos da lista
    def print_list(self):
        pointer = self.head
        while pointer:
            print(f"{pointer.data}\n")
            pointer = pointer.next

    # metodo para definir o tamanho da lista de forma pythonica
    def __len__(self):
        return self.size
    
    # metodo para remove elemento da lista
    def remove(self, aula):
        # se o elemento escolhido for o primeiro
        if aula == self.head.data:
            # cabeça recebe segundo elemento
            self.head = self.head.next
            # decrementa 1 (diminui o tamanho da lista)
            self.size -= 1
            return
        
        # define ponteiro que aponta para primeiro elemento da lista
        pointer = self.head
        # define ponteiro anterior
        previous = None
        # enquanto ponteiro não for none
        while pointer:
            # se o elemento for igual a aula escolhida
            if pointer.data == aula:
                # aula anterior da aula escolhida aponta para proxima aula da aula escolhida
                previous.next = pointer.next
                # decrementa 1 (diminui o tamanho da lista)
                self.size -= 1
                return
            
            # atuliza ponteiros
            previous = pointer
            pointer = pointer.next

    # metodo para adicionar elemento em uma lista
    def to_list(self):
        lista_aulas = []
        pointer = self.head
        while pointer:
            lista_aulas.append(pointer.data)
            pointer = pointer.next
        return lista_aulas
