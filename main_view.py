import tournament_view
import player_view


class View:
    def launch(self):
        tournaments_view = tournament_view.TournamentView()
        self.tournament = tournaments_view.register_tournament()
        players_view = player_view.PlayersView()
        for _ in range(4):
            player = players_view.register_player()
            self.tournament.add_player(player)
            return self.tournament.players_list()
        self.tournament.add_player_groupe()
        return (
            self.tournament.groupe1,
            self.tournament.groupe2,
            self.tournament.groupe3,
            self.tournament.groupe4,
        )


p = View()
p.launch()
