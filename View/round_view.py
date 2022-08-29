class MatchView:
    @staticmethod
    def get_match_result(player_1, player_2):
        match_result = None
        while match_result not in ("1", "2", "3"):
            match_result = input(
                f"Résultat match {player_1} VS {player_2} (1, 2, 3): ")
        return match_result

    def end_match(self, player_1, player_2):
        print("\nResultat du match?")
        print(f"1: {player_1}")
        print(f"2: {player_2}")
        print("3: Draw\n")
        match_result = self.get_match_result(player_1, player_2)
        if match_result == "1":
            print(f"{player_1} a gagné!")
        elif match_result == "2":
            print(f"{player_2} a gagné!")
        elif match_result == "3":
            print("Match nul")
        return match_result

    def display(match_or_round):
        print(match_or_round)
