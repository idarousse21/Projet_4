import tournamentview
import playersview
class View:
    def launch(self):
        tournament_view = tournamentview.TournamentView()
        tournament = tournament_view.register_tournament()
        player_view = playersview.PlayersView()
        for _ in range(2):
            player = player_view.register_player()
            tournament.add_player(player)
            print(tournament.players_list)
p = View()
p.launch()