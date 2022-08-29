from tinydb.operations import add
from db import database


class TournamentModel:
    tournament_table = database.table("tournaments")

    def __init__(
        self,
        tournament_name,
        tournament_venue,
        tournament_start_date,
        tournament_end_date,
    ):
        self.id = None
        self.tournament_name = tournament_name
        self.tournament_venue = tournament_venue
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.players_list = []
        self.rounds = []

        self.initial_save()

    def __repr__(self):
        return f"{self.tournament_name} ({self.tournament_venue})"

    def initial_save(self):
        self.id = self.tournament_table.insert(
            {
                "tournament_name": self.tournament_name,
                "tournament_venue": self.tournament_venue,
                "tournament_start_date": self.tournament_start_date,
                "tournament_end_date": self.tournament_end_date,
                "players": [],
                "rounds": [],
            }
        )

    def add_player(self, player):
        self.players_list.append(player)
        self.tournament_table.update(
            add("players", [{"id": player.id}]),
            doc_ids=[self.id],
        )

    def add_round(self, round_):
        self.rounds.append(round_)
        self.tournament_table.update(
            add("rounds", [{"id": round_.id}]),
            doc_ids=[self.id],
        )

    def have_already_played(self, player_1, player_2) -> bool:
        for round_ in self.rounds:
            if round_.have_already_played(player_1, player_2):
                return True
        return False

    @classmethod
    def get_tournament_list(cls):
        return cls.tournament_table
