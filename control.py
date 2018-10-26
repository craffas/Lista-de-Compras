#Classe de Controle
class Control:
    #Método Construtor
    def __init__(self, view, model):
        #Atributos
        self.view = view
        self.model = model

    #Método para exibir menu:
    def exibir_menu(self):
        #Acionar o método da classe View
        self.view.exibir_menu()

    #Método para recuperar a lista de compras:
    def get_lista_compras(self):
        #Acionar o método da classe View
        return self.model.get_lista_compras()

    #Método para adicionar na lista:
    def add_item_lista(self):
        chave = input('Digite o item: ')
        valor = int(input('Digite a quantidade: '))
        if self.consultar_item(chave) == None:
           self.model.lista_compras.update({chave: valor})
        else:
             self.model.lista_compras[chave] += valor



    #Método de consulta de lista:
    def consultar_item(self, chave):
       return self.model.lista_compras.get(chave)


    #Método para remover na lista:
    def remove_item_lista(self):
        chave = input('Digite o item: ')
        self.model.lista_compras.pop(chave)


