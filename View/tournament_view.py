class TournamentView:

    FIELDS_REGISTRATION = {
        "tournament_name": "Enregistrer le nom du tournoi: ",
        "tournament_venue": "Enregistrer le lieu du tournoi: ",
        "tournament_start_date": "Date de début du tournoi (jjmmaaaa): ",
        "tournament_end_date": "Date de fin du tournoi (jjmmaaaa): ",
        "choice_tournament": "Choix du tournoi (1,2,3...): ",

    }

    @staticmethod
    def register_field(field):
        to_display = TournamentView.FIELDS_REGISTRATION[field]
        field = input(f"\n{to_display}")
        return field

    def display_invalid(field):
        print(f"{field} invalide")

    def display_final_leaderboard(sorted_players_list):
        for number, player in enumerate(sorted_players_list, 1):
            print(f"{number} {player}")

    def display_leaderboard(list_player):
        print(f"{list_player}\n")

    def tournament_display(tournament):
        print(tournament)
