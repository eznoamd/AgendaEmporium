from .ConectorMySQL import ConectorMySQL

class AdapterDatabase:
    def __init__(self):
        self.conector = ConectorMySQL()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        return self.conector.connect()

    def close(self):
        self.conector.close()

    def desative_line(self, obj):
        return self.conector.desative_line(obj)

    def ative_line(self, obj):
        return self.conector.ative_line(obj)

    def select(self, obj, id=None):
        return self.conector.select(obj, id)
    
    def insert(self, obj):
        return self.conector.insert(obj)

    def update(self, obj):
        return self.conector.update(obj)
