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
        self.group_top_ranking = []
        self.group_bottom_ranking = []

    def __repr__(self):
        return str(
            {
                "tournament_name": self.tournament_name,
                "tournament_venue": self.tournament_venue,
                "tournament_start_date": self.tournament_start_date,
                "tournament_end_date": self.tournament_end_date,
                "number_turns": self.number_turns,
            }
        )

    def add_player(self, player):
        self.players_list.append(player)

    def add_player_groupe(self):
        p = sorted(self.players_list, key=lambda players_list: players_list.ranking)
        for player in p[:2]:
            self.group_top_ranking.append(player)
        for player in p[-2:]:
            self.group_bottom_ranking.append(player)

    # def add_player_match(self):
    #     for player in range(2):
    #         self.match1.append(self.groupe1)
    #         self.match2.append(self.groupe2)
