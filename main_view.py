from player_controller import ControllerPlayer
from round_controller import ControllerRound
from tournament_controller import ControllerTournament


class Launcher:

    NB_PLAYERS = 2
    NB_ROUNDS = 1

    def __init__(self):
        self.tournament = None
        self.tournament_controller = ControllerTournament()
        self.player_controller = ControllerPlayer()
        self.round_controller = ControllerRound()

    def launch(self):
        self.tournament = self.tournament_controller.ask_for_tournament_infos()
        for _ in range(self.NB_PLAYERS):
            player = self.player_controller.ask_for_player_infos()
            self.tournament.add_player(player)
        # print(self.tournament.players_list)
        for i in range(self.NB_ROUNDS):
            round_ = self.round_controller.launch_round(self.tournament.players_list, i)
            self.tournament.add_round(round_)

        # self.tournaments_view.display_final_leaderboard()


p = Launcher()
p.launch()
