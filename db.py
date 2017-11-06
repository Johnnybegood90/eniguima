import rethinkdb as r

class Database:

    db_address = ""
    db_port = 0
    db_name = ""

    def __init__(db_address = "localhost", db_port = 28015, db_name = "eniguima"):
        self.db_address = db_address
        self.db_port = db_port
        self.db_name = db_name

    def connect(self):
        r.connect(self.db_address, self.db_port).repl()

    def create_db(db_name = self.db_name):
        if not r-dblist().contains(db_name):
            r.db_create(db_name).run()
