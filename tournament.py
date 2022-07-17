import playersview


class Tournament:
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

    def register_tournament(self):
        self.tournament_name = input("")
        self.tournament_venue = input("")
        self.tournament_start_date = input("")
        self.tournament_end_date = input("")
        Tournament.choice_player()
        return {
            "tournament_name": self.tournament_name,
            "tournament_venue": self.tournament_venue,
            "tournament_start_date": self.tournament_start_date,
            "tournament_end_date": self.tournament_end_date,
        }

    def choice_player(self):
        tournoi = self.__init__(",", ",", ",", ",")
        for _ in range(7):
            player = playersview.PlayersView()
            tournoi(player)


tournoi = Tournament(",", ",", ",", ",")
tournoi.register_tournament()
