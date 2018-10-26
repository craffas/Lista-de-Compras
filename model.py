#Classe de modelo

class Model:
    #Método Construtor:
    def __init__(self):
        #Atributos:
        self.lista_compras = {'Chocolate': 1, 'Pipoca': 2, 'Refrigerante': 10}

    #Método que recupera a lista:
    def get_lista_compras(self):
        return self.lista_compras

    #Método que inclui item na lista:
