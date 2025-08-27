from database.AdapterDatabase import AdapterDatabase

class ClienteModel:
    def __init__(self):
        self.table = 'cliente'

    def criar_cliente(self, nome, codigo):
        # cria tudo necessario no atual obj para enviar para o banco
        self.nome = nome
        self.codigo = codigo
        self.ativo = 1

        # conecta ao banco e insere o obj
        db = AdapterDatabase()
        db.connect()
        err = db.insert(obj = self)
        db.close()
        
        # verifica se houve erro
        if err is not None:
            return err
        return True
    
    def get_all(self, id):
        #conecta ao banco e pega toda a tabela
        db = AdapterDatabase()
        db.connect()
        listaCliente = db.select(obj = self)
        db.close()
        
        # verifica se houve erro
        if err is not None:
            return err
        return listaCliente