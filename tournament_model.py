import random


class TournamentModel:
    def __init__(
        self,
        tournament_name,
        tournament_venue,
        tournament_start_date,
        tournament_end_date,
    ):
        self.tournament_name = tournament_name
        self.tournament_venue = tournament_venue
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.number_turns = 4
        self.players_list = []
        self.groupe1 = []
        self.groupe2 = []
        self.groupe3 = []
        self.groupe4 = []

    def __repr__(self):
        return str({
            "tournament_name": self.tournament_name,
            "tournament_venue": self.tournament_venue,
            "tournament_start_date": self.tournament_start_date,
            "tournament_end_date": self.tournament_end_date,
            "number_turns": self.number_turns,
        })

    def add_player(self, player):
        self.players_list.append(player)

    def add_player_groupe(self):
        for i in range(2):
            self.groupe1.append(random.choice(self.players_list))
            self.groupe2.append(random.choice(self.players_list))
            self.groupe3.append(random.choice(self.players_list))
            self.groupe4.append(random.choice(self.players_list))
