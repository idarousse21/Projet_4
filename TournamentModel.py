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

    def add_player(self, player):
        self.players_list.append(player)      

    def __repr__(self):
        return {
            "tournament_name": self.tournament_name,
            "tournament_venue": self.tournament_venue,
            "tournament_start_date": self.tournament_start_date,
            "tournament_end_date": self.tournament_end_date,
            "number_turns": self.number_turns,
        }


