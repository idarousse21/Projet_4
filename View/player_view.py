class PlayersView:

    FIELDS_REGISTRATION = {
        "last_name": "Enregistrer votre nom: ",
        "first_name": "Enregistrer votre prénom: ",
        "date_of_birth": "Enregistrer votre date de naissance (jjmmaaaa): ",
        "gender": "Séléctionner h(homme) ou f(femme): ",
        "rank": "Entrer votre rang: ",
        "rank_player": "Classement du joueur: ",
        "new_rank_player": "Nouveau classement: ",
    }

    @staticmethod
    def register_field(field):
        to_display = PlayersView.FIELDS_REGISTRATION[field]
        field = input(f"\n{to_display}")
        return field

    def display_invalid(field):
        print(f"{field} invalide")

    def display_leaderboard(list_player):
        print(list_player)
