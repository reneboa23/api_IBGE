import psycopg2 as db

class Config:

    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "root",
                "host": "localhost",
                "port": "5432",
                "database": "ibge"
            }
        }

class Connection(Config):
    def __init__(self):
        Config.__init__(self)

        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Connection error. ', e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit
        self.connection.close()

    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        return self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
    
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())

        return self.fetchall()

class Database(Connection):

    def __init__(self):
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO tb_municipios (municipio, uf, sigla_uf, regiao) VALUES (%s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print('Insertion error. ', e)

    def select(self):
        sql = "SELECT * FROM tb_municipios"
        row = self.query(sql)

        return row
    
    def select_id(self, id):
        sql = f"SELECT id, municipio, sigla_uf, uf, regiao FROM public.tb_municipios where id = {id}"
        row = self.query(sql)

        return row
    
    def get_all(self):
        rows = self.select()

        municipios = []
        
        for data in rows:
            municipios.append({'id': data[0], 'municipio': data[1], 'uf': data[2], 'sigla_uf': data[3], 'regiao': data[4]})

        return municipios

    def get_mun(self, id):
        row = self.select_id(id)

        return {'id': row[0][0], 'municipio': row[0][1], 'uf': row[0][2], 'sigla_uf': row[0][3], 'regiao': row[0][4]}

        