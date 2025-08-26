import mysql.connector
import os
from dotenv import load_dotenv

class ConectorMySQL:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        load_dotenv()
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        self.cur = self.conn.cursor(dictionary=True)
        return self.conn

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def desative_line(self, obj):
        query = f"UPDATE {obj.table} SET ativo = 0 WHERE id = %s"
        self.cur.execute(query, (obj.id,))
        self.conn.commit()

    def ative_line(self, obj):
        query = f"UPDATE {obj.table} SET ativo = 1 WHERE id = %s"
        self.cur.execute(query, (obj.id,))
        self.conn.commit()

    def select(self, obj, id=None):
        if id is None:
            query = f"SELECT * FROM {obj.table}"
            self.cur.execute(query)
        else:
            query = f"SELECT * FROM {obj.table} WHERE id = %s"
            self.cur.execute(query, (id,))
        return self.cur.fetchall()

    def insert(self, obj):
        keys = [k for k in obj.__dict__.keys() if k != "table"]
        values = [getattr(obj, k) for k in keys]
        placeholders = ", ".join(["%s"] * len(values))
        query = f"INSERT INTO {obj.table} ({', '.join(keys)}) VALUES ({placeholders})"
        self.cur.execute(query, tuple(values))
        self.conn.commit()

    def update(self, obj):
        keys = [k for k in obj.__dict__.keys() if k not in ("table", "id")]
        values = [getattr(obj, k) for k in keys]
        set_clause = ", ".join([f"{k} = %s" for k in keys])
        query = f"UPDATE {obj.table} SET {set_clause} WHERE id = %s"
        self.cur.execute(query, tuple(values) + (obj.id,))
        self.conn.commit()
