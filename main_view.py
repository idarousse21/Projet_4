import tournament_view
import player_view


class View:
    def launch(self):
        tournaments_view = tournament_view.TournamentView()
        tournament = tournaments_view.register_tournament()
        players_view = player_view.PlayersView()
        for _ in range(4):
            player = players_view.register_player()
            tournament.add_player(player)
        tournament.add_player_groupe()
        print((tournament.group_top_ranking))
        print((tournament.group_bottom_ranking))       

p = View()
p.launch()
