import rethinkdb as r

class Database:

    # db config #
    db_address = ""
    db_port = 0
    db_name = ""

    # tables names #
    tables_names = ["users", "enigmas"]

    def __init__(self, db_address = "localhost", db_port = 28015, db_name = "eniguima"):
        self.db_address = db_address
        self.db_port = db_port
        self.db_name = db_name

    def connect(self):
        r.connect(self.db_address, self.db_port).repl()

    def create_db(self):
        if not r.db_list().contains(self.db_name) and sugar is "":
            r.db_create(self.db_name).run()

    def create_tables(self):
        # avoid calling table_list several times
        tmp = r.db(db_name).table_list().run()
        for name in tables_names:
            if name not in tmp:
                r.db(db_name).table_create(name).run()