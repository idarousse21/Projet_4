import re
from datetime import datetime

from Model.player_model import PlayersModel
from View.player_view import PlayersView


def is_valid_name(name):
    regex = r"^[a-zA-Z\s\-']+$"
    return bool(re.match(regex, name))


class ControllerPlayer:

    def __init__(self):
        self.player = None

    def ask_for_player_infos(self):
        last_name = self.register_last_name()
        first_name = self.register_first_name()
        date_of_birth = self.register_date_of_birth()
        gender = self.register_gender()
        rank = self.register_ranking()
        self.player = PlayersModel(
            last_name, first_name, date_of_birth, gender, rank)
        return self.player

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
                PlayersView.display_invalid(first_name)
            else:
                return first_name

    @staticmethod
    def register_date_of_birth():
        while True:
            date_of_birth = PlayersView.register_field("date_of_birth")
            if not len(date_of_birth) == 8 and date_of_birth.isdigit():
                PlayersView.display_invalid(date_of_birth)
            else:
                date_of_birth = datetime.strptime(
                    date_of_birth, "%d%m%Y").strftime("%d/%m/%Y")
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
                PlayersView.display_invalid(gender)

    @staticmethod
    def register_ranking():
        while True:
            rank = PlayersView.register_field("rank")
            if not rank.isdigit() or int(rank) <= 0:
                PlayersView.display_invalid(rank)
            else:
                return int(rank)

    def change_player_ranking(self, player_list):
        choice_player = int(PlayersView.register_field("rank_player"))
        for player in player_list:
            if player.rank == choice_player:
                chang_rank = int(PlayersView.register_field("new_rank_player"))
                if chang_rank > 0:
                    player.update_ranking(chang_rank)
                    break
                else:
                    PlayersView.display_invalid(chang_rank)
            else:
                PlayersView.display_invalid(choice_player)

    def ranking_all_player(self, choice):
        players_list = sorted(
            PlayersModel.get_players_list(), key=lambda player: player[choice]
        )
        players_list = "\n".join(map(str, players_list))
        PlayersView.display_leaderboard(
            players_list.replace("'", "")
            .replace("}", "")
            .replace("{", "")
            .replace(",", "")
        )

    def ranking_tournament(self, choice, tournament):
        players_list = []
        for players in tournament:
            player_id = players.get("id")
            player = PlayersModel.player_table.get(doc_id=player_id)
            players_list.append(player)
        player = sorted(players_list, key=lambda player: player[choice])
        player = "\n".join(map(str, players_list))
        PlayersView.display_leaderboard(
            player.replace("'", "")
            .replace("}", "")
            .replace("{", "")
            .replace(",", "")
        )
