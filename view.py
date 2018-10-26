#Classe de Visualização

class View:
    #Método Construtor:
    def __init__(self):
        self.control = None

    #Guarda a Control associada
    def set_control(self, control):
        self.control = control


    #Método de Exibição do menu:
    def exibir_menu(self):
        resposta = True
        #Exibir menu:
        while resposta:
            print('''
            1. Exibir Lista.
            2. Incluir Item.
            3. Excluir Item.
            4. Sair.
            ''')

            #Solicitando opção:
            resposta = input('Digite um número: ')

            #Verificando a resposta:

            if resposta == '1':
                print("\nLista de itens: ")
                self.exibir_lista_compras(self.control.get_lista_compras())

            elif resposta == '2':
                self.control.add_item_lista()
                print('\nItem incluído.')


            elif resposta == '3':
                self.control.remove_item_lista()
                print('\nItem excluído.')

            elif resposta == '4':
                print('\nTchau!.')
                resposta = False
            else:
                print('\nValor inválido!')

    #Método para exibir lista de compras:
    def exibir_lista_compras(self, lista_compras):
        #A lista de compras é um dicionário:
        #Percorrer o dicionário
        for chave, valor in lista_compras.items():
            print(f'-{chave} : {valor}')
