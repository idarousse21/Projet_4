class TournamentView:

    FIELDS_REGISTRATION = {
        "tournament_name": "Enregistrer le nom du tournoi: ",
        "tournament_venue": "Enregistrer le lieu du tournoi: ",
        "tournament_start_date": "Enregistrer la date de début du tournoi (jjmmaaaa): ",
        "tournament_end_date": "Enregistrer la date de fin du tournoi (jjmmaaaa): ",
    }

    @staticmethod
    def register_field(field):
        to_display = TournamentView.FIELDS_REGISTRATION[field]
        field = input(to_display)
        return field

    def display_invalid(field):
        print(f"{field} invalide")
