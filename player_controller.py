import re
from datetime import datetime

from player_model import PlayersModel
from player_view import PlayersView


def is_valid_name(name):
    regex = r"^[a-zA-Z\s\-']+$"
    return bool(re.match(regex, name))


class ControllerPlayer:
    def ask_for_player_infos(self):
        last_name = "abc" # self.register_last_name()
        first_name = "dev" # self.register_first_name()
        date_of_birth = self.register_date_of_birth()
        gender = "f" # self.register_gender()
        ranking = 3 # self.register_ranking()
        player = PlayersModel(last_name, first_name, date_of_birth, gender, ranking)
        return player

    @staticmethod
    def register_last_name():
        while True:
            last_name = PlayersView.register_field("last_name")
            if not is_valid_name(last_name):
                PlayersView.display_invalid(last_name)
            else:
                return last_name

    @staticmethod
    def register_first_name():
        while True:
            first_name = PlayersView.register_field("first_name")
            if not is_valid_name(first_name):
                print("Prénom invalide")
            else:
                return first_name

    @staticmethod
    def register_date_of_birth():
        while True:
            date_of_birth = PlayersView.register_field("date_of_birth")
            if not len(date_of_birth) == 8 and date_of_birth.isdigit():
                print("Date de naissance invalide")
            else:
                date_of_birth = datetime.strptime(date_of_birth, "%d%m%Y").strftime(
                    "%d/%m/%Y"
                )
                return date_of_birth

    @staticmethod
    def register_gender():
        while True:
            gender = PlayersView.register_field("gender")
            if gender == "h":
                gender = "Homme"
                return gender
            elif gender == "f":
                gender = "Femme"
                return gender
            else:
                print("Genre invalide")

    @staticmethod
    def register_ranking():
        while True:
            ranking = PlayersView.register_field("ranking")
            if not ranking.isdigit() or int(ranking) <= 0:
                print("Rang invalide")
            else:
                return int(ranking)
