from database.AdapterDatabase import AdapterDatabase

class TipoModel:
    def __init__(self, id=None, nome=None, filtros=None, ativo=None):
        self.table = 'tipo'

        '''
        Isso aqui em baixo e nos parametros
        '''
        self.id = id
        self.nome = nome
        self.filtros = filtros
        self.ativo = ativo

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
    
    def deletar_tipo(self, id):
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
        listaTipo = db.select(obj = self)
        db.close()
        
        # verifica se houve erro
        if err is not None:
            return err
        return listaTipo
    
    '''
    Isso aqui em baixo
    '''
    def get_by_id(self, id):
        #conecta ao banco e pega toda a tabela
        db = AdapterDatabase()
        db.connect()
        listaTipo = db.select(obj = self, id = id)
        db.close()
        
        # verifica se houve erro
        if err is not None:
            return err
        return listaTipo

