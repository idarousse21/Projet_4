from tinydb import TinyDB

database = TinyDB("db.json")
tournament_table = database.table("tournaments")
