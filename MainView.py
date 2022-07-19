import tournamentview
import playersview
class View:

    def launch(self):
        tournament_view = tournamentview.TournamentView()
        self.tournament = tournament_view.register_tournament()
        player_view = playersview.PlayersView()
        for _ in range(4):
            player = player_view.register_player()
            p = self.tournament.add_player(player)
            return self.tournament.players_list()
        self.tournament.add_player_groupe()
        return self.tournament.groupe1, self.tournament.groupe2, self.tournament.groupe3, self.tournament.groupe4


    

p = View()
p.launch()
