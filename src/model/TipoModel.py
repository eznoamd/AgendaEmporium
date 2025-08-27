from database.AdapterDatabase import AdapterDatabase

class TipoModel:
    def __init__(self):
        self.table = 'Tipo'

    def criar_tipo(self, nome, filtros):
        # cria tudo necessario no atual obj para enviar para o banco
        self.nome = nome
        self.filtros = filtros
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