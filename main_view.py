from Controller.player_controller import ControllerPlayer
from Controller.round_controller import ControllerRound
from Controller.tournament_controller import ControllerTournament


class Launcher:

    NB_PLAYERS = 8
    NB_ROUNDS = 4
    launcher_start_list = {
        "1": "1: Lancement du tournoi",
        "2": "2: Classement joueur",
        "3": "3: Classement joueur d'un tournoi",
        "4": "4: Liste des tournois",
        "5": "5: Liste des tours d'un tournoi",
        "6": "6: Liste des matchs d'un tournoi",
        "7": "7: Quitter",
    }
    rank_or_alphabetical = {
        "1": "1: Ordre alphabétique",
        "2": "2: Ordre par rang"}

    change_in_rank = {
        "1": "Voulez-vous modifié le classement d'un joueur ?",
        "2": "1: Oui",
        "3": "2: Non",
    }

    def __init__(self):
        self.tournament = None
        self.tournament_controller = ControllerTournament()
        self.player_controller = ControllerPlayer()
        self.round_controller = ControllerRound()

    def display_launch_choice(launcher_list):
        for launcher_choice in launcher_list.values():
            print(launcher_choice)

    def launch(self):
        while True:
            Launcher.display_launch_choice(self.launcher_start_list)
            launch_choice = input("\nChoix: ")
            if launch_choice == "1":
                Launcher.tournament_launch(self)
            elif launch_choice == "2":
                Launcher.display_launch_choice(self.rank_or_alphabetical)
                choice_order = input("\nChoix: ")
                if choice_order == "1":
                    self.player_controller.ranking_all_player("last_name")
                elif choice_order == "2":
                    self.player_controller.ranking_all_player("rank")
            elif launch_choice == "3":
                Launcher.display_launch_choice(self.rank_or_alphabetical)
                choice_order = input("\nChoix: ")
                if choice_order == "1":
                    tournament = self.tournament_controller.tournament_pick(
                        "players")
                    self.player_controller.ranking_tournament(
                        "last_name", tournament)
                elif choice_order == "2":
                    tournament = self.tournament_controller.tournament_pick(
                        "players")
                    self.player_controller.ranking_tournament(
                        "rank", tournament)
            elif launch_choice == "4":
                self.tournament_controller.tournament_list()
            elif launch_choice == "5":
                tournament = self.tournament_controller.tournament_pick(
                    "rounds")
                self.round_controller.tournament_rounds(tournament)

            elif launch_choice == "6":
                tournament = self.tournament_controller.tournament_pick(
                    "rounds")
                self.round_controller.tournament_matches(tournament)
            elif launch_choice == "7":
                break

    def tournament_launch(self):
        self.tournament = self.tournament_controller.ask_for_tournament_infos()
        for _ in range(self.NB_PLAYERS):
            player = self.player_controller.ask_for_player_infos()
            self.tournament.add_player(player)
        for i in range(self.NB_ROUNDS):
            round_ = self.round_controller.launch_round(
                self.tournament.players_list, i)
            self.tournament.add_round(round_)
            Launcher.choice_change_rank(self)
        self.tournament_controller.display_final_leaderboard(
            self.tournament.players_list
        )
        Launcher.choice_change_rank(self)

    def choice_change_rank(self):
        while True:
            Launcher.display_launch_choice(self.change_in_rank)
            choice_launch = input("\nChoix: ")
            if choice_launch == "1":
                self.player_controller.change_player_ranking(
                    self.tournament.players_list
                )
            elif choice_launch == "2":
                break


p = Launcher()
p.launch()
