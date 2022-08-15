from db import database


class PlayersModel:

    DB_TABLE_NAME = "players"

    def __init__(self, last_name, first_name, date_of_birth, gender, ranking):
        self.id = None
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = 0

        self.player_table = database.table(self.DB_TABLE_NAME)

        self.initial_save()

    def __repr__(self):
        return f"Joueur:{self.last_name} {self.first_name} Rang:{self.ranking} Score:{self.score}"

    def initial_save(self):
        self.id = self.player_table.insert(
            {"last_name": self.last_name, "first_name": self.first_name}
        )

    def add_score(self, addition):
        self.score += addition
