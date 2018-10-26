#Programa Principal
#Importação de calsses:
from view import View
from control import Control
from model import Model

#Instanciar a Model:
m = Model()
#Instanciar a View:
v = View()
#Instanciar a Control:
c = Control(v, m)
#Guardando a Control na View:
v.set_control(c)
#Exibir Menu
c.exibir_menu()