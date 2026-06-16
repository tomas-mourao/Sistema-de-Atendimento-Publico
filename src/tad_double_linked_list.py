# -----------------------------------------------------------------------------------
#                      
#                          NOTICE: RESTRICTED EDITING ZONE
#
#    You are only allowed to edit this file in the sections clearly marked for edits.
#      Any changes outside the allowed regions may be overwritten or cause errors.
#
#      Please follow the guidelines and only modify code where it explicitly says:
#                       >>> YOU MAY EDIT BELOW THIS LINE <<<
#
#            If you are unsure, consult your teacher or project supervisor.
#
# -----------------------------------------------------------------------------------

from src.node import Node

class TADDoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        self.__head = value

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, value):
        self.__tail = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def is_empty(self):
        return self.size == 0

    def add_tail(self, person):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        new_node = Node(person)
        if self.is_empty(): #se tiver vazio, head e tail são o mesmo elemento
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail #ligar o novo no ao ultimo elemento da lista
            self.tail.next = new_node #ligamos o ultimo no ao novo elemento
            self.tail = new_node #atualizar a tail para o ultimo elemento
        self.size += 1

    def remove_head(self):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        if self.is_empty(): #se tiver vazio nao tem head
            return None

        removed_node = self.head #o nó a remover é o da head
        if self.head == self.tail: # se tiver apenas um elemento
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next #head passa para o elemento seguinte
            self.head.prev = None #remover a ligacao ao elemento anterior
        self.size -= 1
        return removed_node.person

    def find(self, ticket):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        current = self.head #começa no início da fila
        while current is not None: #percorrer a lista toda
            if current.person.ticket == ticket: #se o ticket coincidir
                return current # returnamos o elemento
            current = current.next #para continuar a ver a lista enquanto não acha
        return None #caso não haja

    def remove_node(self, node):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        if self.is_empty() or node is None:     #verifica se a lista está vazia e se tem algo no node
            return None

        if node is self.head: # se o node escolhido for a head
            return self.remove_head() #remover a head (atualiza automaticamente a cabeça e o tamanho)

        if node is self.tail: #se for a tail
            if self.tail.prev is None: # se só houver 1 elemento
                self.head = None
                self.tail = None
            else: #se houver mais do que um elemento
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            return node.person

        #caso não seja a cabeça nem a tail
        node.prev.next = node.next #atualiza a ligação do no anterior
        node.next.prev = node.prev #depois atualizamos a do nó seguinte
        self.size -= 1
        return node.person

    def get_all_nodes(self):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        nodes = [] #aramzenar os nós

        current = self.head #comecar no início
        while current is not None: #percorre a lista
            person = current.person # person vai ser a informação da pessoa atual
            nodes.append((person.ticket, person.name, person.type)) #adicionar um tuplo com os dados da pessoa a nodes
            current = current.next
        return nodes