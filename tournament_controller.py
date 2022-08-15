from datetime import datetime

from tournament_model import TournamentModel
from tournament_view import TournamentView

special_characters = "-' "


def convert(s):
    new = ""
    for x in s:
        new += x
    return new


class ControllerTournament:
    def ask_for_tournament_infos(self):
        tournament_name = "name"  # self.register_tournament_name()
        tournament_venue = "venue"  # self.register_tournament_venue()
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
            alphabet_letter = (
                x for x in tournament_name if x not in special_characters
            )
            tournament_name_converter = convert(alphabet_letter)
            if not tournament_name_converter.isalpha():
                print("Nom invalide")
            else:
                return tournament_name

    @staticmethod
    def register_tournament_venue():
        while True:
            tournament_venue = TournamentView.register_field("tournament_venue")
            alphabet_letter = (
                x for x in tournament_venue if x not in special_characters
            )
            tournament_venue_converter = convert(alphabet_letter)
            if not tournament_venue_converter.isalpha():
                print("Nom invalide")
            else:
                return tournament_venue

    @staticmethod
    def register_tournament_start_date():
        while True:
            tournament_start_date = TournamentView.register_field(
                "tournament_start_date"
            )
            if not len(tournament_start_date) == 8 and tournament_start_date.isdigit():
                print("Date invalide")
            else:
                tournament_start_date = datetime.strptime(
                    tournament_start_date, "%d%m%Y"
                ).strftime("%A %d %B %Y")
                return tournament_start_date

    @staticmethod
    def register_tournament_end_date():
        while True:
            tournament_end_date = TournamentView.register_field("tournament_end_date")
            if not len(tournament_end_date) == 8 and tournament_end_date.isdigit():
                print("Date invalide")
            else:
                tournament_end_date = datetime.strptime(
                    tournament_end_date, "%d%m%Y"
                ).strftime("%A %d %B %Y")
                return tournament_end_date
