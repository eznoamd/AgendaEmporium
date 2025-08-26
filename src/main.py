# Usa esse arquivo main.py para testar as 
# classes que tu for colocar na model

# Entra na pasta src pelo terminal
# Executa: 
# python main.py
# ou 
# py main.py

class TesteBanco:
    def __init__(self):
        self.table = 'TesteBanco'
        self.id = 1
        self.descricao = "trocado"

from model.database.AdapterDatabase import AdapterDatabase

adapter = AdapterDatabase()
adapter.connect()
print(adapter.delete(TesteBanco()))
adapter.close()
