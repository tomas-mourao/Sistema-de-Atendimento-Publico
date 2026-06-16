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

from typing import Type

from src.person import Person
from src.tad_simple_list import TADSimpleList
from src.tad_double_linked_list import TADDoublyLinkedList

from datetime import datetime

class AttendanceSystem:

    def __init__(self, TAD_CLASS: Type[TADDoublyLinkedList | TADSimpleList]):
        self.__normal_queue = TAD_CLASS()
        self.__priority_queue = TAD_CLASS()
        self.__ticket_counters = {
            "A": 0, "B": 0,
            "C": 0, "D": 0,
            "E": 0
        }
        self.__priority_served_count = 0
        self.__total_served = 0
        
    @property
    def normal_queue(self):
        return self.__normal_queue
    
    @normal_queue.setter
    def normal_queue(self, value):
        self.__normal_queue = value
    
    @property
    def priority_queue(self):
        return self.__priority_queue
    
    @priority_queue.setter
    def priority_queue(self, value):
        self.__priority_queue = value
    
    @property
    def ticket_counters(self):
        return self.__ticket_counters
    
    @ticket_counters.setter
    def ticket_counters(self, value):
        self.__ticket_counters = value
    
    @property
    def priority_served_count(self):
        return self.__priority_served_count
    
    @priority_served_count.setter
    def priority_served_count(self, value):
        self.__priority_served_count = value
    
    @property
    def total_served(self):
        return self.__total_served
    
    @total_served.setter
    def total_served(self, value):
        self.__total_served = value

    def generate_ticket(self, attendance_type):
        self.ticket_counters[attendance_type] += 1
        number = self.ticket_counters[attendance_type]
        return f"{attendance_type}{number:03d}"

    def get_queues(self):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        return {
            'normal': self.normal_queue.get_all_nodes(),
            'priority': self.priority_queue.get_all_nodes() #acede às filas e retira as informações das pessoas
        } #retorna as pessoas em dicionario
        
    def issue_ticket(self, name, phone, bi, attendance_type):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        ticket = self.generate_ticket(attendance_type) #guarda o ticket da pessoa com o tipo de atendimento (a funcao generate_ticket gera o ticket)
        person = Person(name, phone, bi, attendance_type, ticket) #criar a pessoa com os dados dela
        if attendance_type == 'B': #se for prioritário
            self.priority_queue.add_tail(person)
        else:
            self.normal_queue.add_tail(person)

        person.arrival_time = datetime.now() #hora de chegada da pessoa (a pessoa chegou na hora X)
        return person

    def call_next(self):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        if self.priority_queue.size == 0 and self.normal_queue.size == 0: #se as filas estiverem vazias
            return None

        elif self.priority_served_count < 2 and self.priority_queue.size > 0: #se ainda faltar chamar prioritarios (caso ainda haja para atender)
            person = self.priority_queue.remove_head() #é chamado (remove da fila)
            self.priority_served_count += 1 # adicionamos 1 à contagem de prioritários servidos

        elif self.normal_queue.size > 0: #se houver gente no normal
            person = self.normal_queue.remove_head() #é chamado (remove da fila)
            self.priority_served_count = 0 #após atender normal, reinicia a contagem de prioritários (regra 2:1)

        else: #se não houver clientes normais, continua a atender prioritários
            person = self.priority_queue.remove_head() #é chamado (remove da fila)

        self.total_served += 1

        person.service_time = datetime.now() #guarda o tempo de atendimento (a pessoa comecou a ser atendida na hora Y)
        return person

    def search_ticket(self, ticket):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        node = self.priority_queue.find(ticket) #econtrar o bilhete na fila dos prioritários
        if node: #se encontrar
            return 'priority', node.person # retornar o tipo de atendimento e a informação da pessoa

        node = self.normal_queue.find(ticket) #encontrar bilhete no atendimento normal
        if node: #se encontrar
            return 'normal', node.person #retornar o tipo de atendimento e a informação dessa pessoa

        return None #caso nao encontre

    def remove_ticket(self, ticket):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        node = self.priority_queue.find(ticket) #encontrar o bilhete no prioritario
        if node: #se econtrar
            self.priority_queue.remove_node(node) #remover o ticket
            return True #devolver true (porque foi removido)

        node = self.normal_queue.find(ticket) #econtrar o bilhete no normal
        if node: #se encontrar
            self.normal_queue.remove_node(node) #remove o ticket
            return True

        return False #se nao encontrar

    def statistics(self):
        # -------------------------------------------------------------------------------------
        #                          >>> YOU MAY EDIT BELOW THIS LINE <<<
        #--------------------------------------------------------------------------------------
        return {
            'total_served' : self.total_served,
            'normal_waiting' : self.normal_queue.size,
            'priority_waiting' : self.priority_queue.size,
        } #para devolver o dicionario
