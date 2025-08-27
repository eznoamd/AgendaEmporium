from database.AdapterDatabase import AdapterDatabase

class StatusModel:
    def __init__(self):
        self.table = 'status'

    def criar_status(self, nome, cor):
        # cria tudo necessario no atual obj para enviar para o banco
        self.nome = nome
        self.cor = cor
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
    
    def deletar_status(self, id):
        # conecta ao banco e deleta o obj
        db = AdapterDatabase()
        db.connect()
        err = db.desative_line(obj = self)
        db.close()
        
        # verifica se houve erro
        if err is not None:
            return err
        return True
    
    def get_all(self):
        #conecta ao banco e pega toda a tabela
        db = AdapterDatabase()
        db.connect()
        listaStatus = db.select(obj = self)
        db.close()
        
        # verifica se houve erro
        if err is not None:
            return err
        return listaStatus