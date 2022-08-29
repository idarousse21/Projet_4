from db import database


class PlayersModel:

    player_table = database.table("players")

    def __init__(self, last_name, first_name, date_of_birth, gender, rank):
        self.id = None
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rank = rank
        self.score = 0
        self.initial_save()

    def __repr__(self):
        name = f"{self.last_name} {self.first_name}"
        return f"{name} Rang:{self.rank} Score:{self.score}"

    def initial_save(self):
        self.id = self.player_table.insert(
            {
                "last_name": self.last_name,
                "first_name": self.first_name,
                "date_of_birth": self.date_of_birth,
                "gender": self.gender,
                "rank": self.rank,
            }
        )

    def add_score(self, addition):
        self.score += addition

    def update_ranking(self, rank):
        self.rank = rank
        self.player_table.update({"rank": rank}, doc_ids=[self.id])

    @classmethod
    def get_players_list(cls):
        for player in cls.player_table:
            yield player
