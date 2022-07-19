from datetime import datetime
import player_model


class PlayersView:
    def register_player(self):
        last_name = self.register_last_name()
        first_name = self.register_first_name()
        date_of_birth = self.register_date_of_birth()
        gender = self.register_gender()
        ranking = self.register_ranking()
        player = player_model.PlayersModel(
            last_name, first_name, date_of_birth, gender, ranking
        )
        return player

    @staticmethod
    def register_last_name():
        while True:
            last_name = input("Enregistrer votre nom: ")
            if not last_name.isalpha():
                print("Nom invalide")
            else:
                return last_name

    @staticmethod
    def register_first_name():
        while True:
            first_name = input("Enregistrer votre prénom: ")
            if not first_name.isalpha():
                print("Prénom invalide")
            else:
                return first_name

    @staticmethod
    def register_date_of_birth():
        while True:
            date_of_birth = input("Enregistrer votre jour de naissance (jjmmaaaa): ")
            if not date_of_birth.isdigit():
                print("Date de naissance invalide")
            else:
                date_of_birth = datetime.strptime(date_of_birth, "%d%m%Y").strftime(
                    "%d/%m/%Y"
                )
                return date_of_birth

    @staticmethod
    def register_gender():
        while True:
            gender = input("Séléctionner homme ou femme pour le choix de votre sexe: ")
            if gender == "homme":
                return gender
            elif gender == "femme":
                return gender
            else:
                print("Genre invalide")

    @staticmethod
    def register_ranking():
        while True:
            ranking = input("Entrer votre rang: ")
            if not ranking.isdigit() or ranking <= "0":
                print("Rang invalide")
            else:
                return ranking
