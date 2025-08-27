from database.AdapterDatabase import AdapterDatabase

class TecnicaModel:
    def __init__(self):
        self.table = 'tecnica'

    def criar_tecnica(self, nome):
        # cria tudo necessario no atual obj para enviar para o banco
        self.nome = nome
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
    
    def deletar_tecnica(self, id):
        #conecta ao banco e desativa o obj
        db = AdapterDatabase()
        db.connect()
        err = db.desative_line(obj = self)
        db.close()
        
        #verifica se houve erro
        if err is not None:
            return err
        return True
    
    def get_all(self, id):
        #conecta ao banco e pega toda a tabela
        db = AdapterDatabase()
        db.connect()
        listaTecnica = db.select(obj = self)
        db.close()
        
        # verifica se houve erro
        if err is not None:
            return err
        return listaTecnica