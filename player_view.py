class PlayersView:

    FIELDS_REGISTRATION = {
        "last_name": "Enregistrer votre nom: ",
        "first_name": "Enregistrer votre prénom: ",
        "date_of_birth": "Enregistrer votre date de naissance (jjmmaaaa): ",
        "gender": "Séléctionner h(homme) ou f(femme) pour le choix de votre sexe: ",
        "ranking": "Entrer votre rang: ",
    }
    @staticmethod
    def register_field(field):
        to_display = PlayersView.FIELDS_REGISTRATION[field]
        field = input(to_display)
        return field

    def display_invalid(field):
        print(f"{field} invalide")
