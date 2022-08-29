import re
from datetime import datetime


from Model.tournament_model import TournamentModel
from View.tournament_view import TournamentView


def is_valid_name(name):
    regex = r"^[a-zA-Z\s\-']+$"
    return bool(re.match(regex, name))


class ControllerTournament:
    def __init__(self):
        self.tournament = None

    def ask_for_tournament_infos(self):
        tournament_name = self.register_tournament_name()
        tournament_venue = self.register_tournament_venue()
        tournament_start_date = self.register_tournament_start_date()
        tournament_end_date = self.register_tournament_end_date()
        self.tournament = TournamentModel(
            tournament_name,
            tournament_venue,
            tournament_start_date,
            tournament_end_date,
        )
        return self.tournament

    @staticmethod
    def register_tournament_name():
        while True:
            tournament_name = TournamentView.register_field("tournament_name")
            if not is_valid_name(tournament_name):
                TournamentView.display_invalid(tournament_name)
            else:
                return tournament_name

    @staticmethod
    def register_tournament_venue():
        while True:
            tournament_venue = TournamentView.register_field(
                "tournament_venue")

            if not is_valid_name(tournament_venue):
                TournamentView.display_invalid(tournament_venue)
            else:
                return tournament_venue

    @staticmethod
    def register_tournament_start_date():
        while True:
            tournament_date = TournamentView.register_field(
                "tournament_start_date")
            if not len(tournament_date) == 8 and tournament_date.isdigit():
                TournamentView.display_invalid(tournament_date)
            else:
                tournament_date = datetime.strptime(
                    tournament_date, "%d%m%Y").strftime("%A %d %B %Y")
                return tournament_date

    def tournament_date_check(date_start, date_end):
        if date_end <= date_start:
            print()

    @staticmethod
    def register_tournament_end_date():
        while True:
            tournament_date = TournamentView.register_field(
                "tournament_end_date")
            if not len(tournament_date) == 8 and tournament_date.isdigit():
                TournamentView.display_invalid(tournament_date)
            else:
                tournament_date = datetime.strptime(
                    tournament_date, "%d%m%Y").strftime("%A %d %B %Y")
                return tournament_date

    def display_final_leaderboard(self, players_list):
        leaderboard = sorted(
            players_list,
            key=lambda player: player.score,
            reverse=True,
        )
        TournamentView.display_final_leaderboard(leaderboard)

    def tournament_pick(self, display_choice):
        tournaments = TournamentModel.get_tournament_list()
        for number, tournament in enumerate(
                range(0, len(list(tournaments))), 1):
            tournament = f"{number}: {tournaments.get(doc_id=tournament + 1)}"
            tournament = (
                tournament.replace("'", "")
                .replace("}", "")
                .replace("{", "")
                .replace(",", "")
            )
            TournamentView.tournament_display(tournament)
        number = TournamentView.register_field("choice_tournament")
        tournament = tournaments.get(doc_id=number)
        id_choice = tournament.get(display_choice)
        return id_choice

    def tournament_list(self):
        tournaments = TournamentModel.get_tournament_list()
        for tournament in range(0, len(list(tournaments))):
            one_tournament = f"{tournaments.get(doc_id=tournament + 1)}\n"
            one_tournament = (
                one_tournament.replace("'", "")
                .replace("}", "")
                .replace("{", "")
                .replace(",", "")
            )
            TournamentView.tournament_display(one_tournament)
