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

class TADSimpleList:

    def __init__(self):
        self.__head = None
        self.__size = 0
        
    @property
    def head(self):
        return self.__head
    
    @head.setter
    def head(self, value):
        self.__head = value
    
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

        if self.is_empty(): #caso esteja fazio
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next  #percorre a lista ate ao ultimo nó
            current.next = new_node    #ligamos o novo nó ao fim da lista
        self.size += 1 #atualizamos o tamanho

    def remove_head(self):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        if self.is_empty():
            return None

        removed_node = self.head #guardar nó a remover
        self.head = self.head.next #avancamos a head
        self.size -= 1
        return removed_node.person #retornamos head a informacao do no removido
    
    def find(self, ticket):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        current = self.head #comecar no primeiro elemento
        while current is not None: #até chegar ao ultimo elemento
            if current.person.ticket == ticket:    #comparamos os tickets
                return current  #retornamos o ticket se for o mesmo
            current = current.next # se nao for igual continua a percorrer a lista, comecando no elemento seguinte
        return None #caso não encontre
    
    def remove_node(self, node):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        if self.is_empty() or node is None: #impossivel remover se a lista estiver vazia ou o nó ser inválido
            return None

        if self.head == node: #caso o no seja logo o primeiro
            return self.remove_head() #remove_head remove a head

        current = self.head
        while current is not None:
            if current.next is node: #encontrar o nó
                removed_node = current.next
                current.next = removed_node.next #alteramos a ligação
                self.size -= 1
                return removed_node.person
            current = current.next
        return None
    
    def get_all_nodes(self):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        result = []

        current = self.head
        while current is not None:
            person = current.person #obter os dados da pessoa
            result.append((person.ticket, person.name, person.type)) #adicionar à lista result o (ticket,nome e tipo)
            current = current.next
        return result