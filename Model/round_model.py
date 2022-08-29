from tinydb.operations import add
from db import database


class RoundModel:
    rounds_table = database.table("rounds")

    def __init__(self):
        self.id = None
        self.matches = []

        self.initial_save()

    def initial_save(self):
        self.id = self.rounds_table.insert({"matches": []})

    def add_match(self, match):
        self.matches.append(match)
        self.rounds_table.update(
            add("matches", [{"id": match.id}]),
            doc_ids=[self.id],
        )

    def have_already_played(self, player_1, player_2):
        for match in self.matches:
            if match.is_between_players(player_1, player_2):
                return True

        return False

    def get_rounds_list(cls):
        return cls.rounds_table


class MatchModel:
    matches_table = database.table("matches")

    def __init__(self, player_1, player_2):
        self.id = None
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None  # If None, it's a draw

        self.initial_save()

    def is_between_players(self, player_1, player_2):
        return {player_1, player_2} == {self.player_1, self.player_2}

    def initial_save(self):
        self.id = self.matches_table.insert(
            {"player_1_id": self.player_1.id, "player_2_id": self.player_2.id}
        )

    def set_winner(self, winner):
        self.winner = winner
        self.matches_table.update(
            {"winner_id": self.winner.id}, doc_ids=[self.id])

    @classmethod
    def get_matches_list(cls):
        return cls.matches_table
