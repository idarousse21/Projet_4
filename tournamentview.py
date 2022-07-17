from datetime import datetime
import TournamentModel


class TournamentView:
    def register_tournament(self):
        tournament_name = self.register_tournament_name()
        tournament_venue = self.register_tournament_venue()
        tournament_start_date = self.register_tournament_start_date()
        tournament_end_date = self.register_tournament_end_date()
        self.display_default_turn()
        tournament = TournamentModel.TournamentModel(
            tournament_name,
            tournament_venue,
            tournament_start_date,
            tournament_end_date,
        )
        return tournament

    @staticmethod
    def register_tournament_name():
        while True:
            tournament_name = input("Enregistrer le nom du tournoi: ")
            if not tournament_name.isalpha():
                print("Nom invalide")
            else:
                return tournament_name

    @staticmethod
    def register_tournament_venue():
        while True:
            tournament_venue = input("Enregistrer le lieu du tournoi: ")
            if not tournament_venue.isalpha():
                print("Nom invalide")
            else:
                return tournament_venue

    @staticmethod
    def register_tournament_start_date():
        while True:
            tournament_start_date = input(
                "Enregistrer la date de début du tournoi (jjmmaaaa): "
            )
            if not tournament_start_date.isdigit():
                print("Date invalide")
            else:
                tournament_start_date = datetime.strptime(
                    tournament_start_date, "%d%m%Y"
                ).strftime("%A %d %B %Y")
                print(tournament_start_date)
                return tournament_start_date

    @staticmethod
    def register_tournament_end_date():
        while True:
            tournament_end_date = input(
                "Enregistrer la date de fin du tournoi (jjmmaaaa): "
            )
            if not tournament_end_date.isdigit():
                print("Date invalide")
            else:
                tournament_end_date = datetime.strptime(
                    tournament_end_date, "%d%m%Y"
                ).strftime("%A %d %B %Y")
                print(tournament_end_date)
                return tournament_end_date

    @staticmethod
    def display_default_turn():
        turn = 4
        print(f"le nombre de tours est de {turn} par default")
