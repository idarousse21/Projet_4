from Model.round_model import MatchModel, RoundModel
from View.round_view import MatchView


class ControllerRound:
    def __init__(self):
        self.match_view = MatchView()

    def build_first_round(self, players_list):
        round_ = RoundModel()
        players = sorted(
            players_list,
            key=lambda player: player.rank,
        )
        group_top_ranking = []
        group_bottom_ranking = []
        for player in players[: int(len(players) / 2)]:
            group_top_ranking.append(player)
        for player in players[-int(len(players) / 2):][::-1]:
            group_bottom_ranking.append(player)
        for player_1, player_2 in zip(group_top_ranking, group_bottom_ranking):
            match = MatchModel(player_1, player_2)
            round_.add_match(match)
        return round_

    def launch_round(self, players_list, is_first_round):
        if is_first_round == 0:
            round_ = self.build_first_round(players_list)
            self.play_round(round_.matches)
        else:
            round_ = self.build_subsequent_round(players_list)
            self.play_round(round_.matches)
        return round_

    def play_round(self, matches):
        for match in matches:
            match_result = self.match_view.end_match(
                match.player_1, match.player_2)
            if match_result == "1":
                match.player_1.add_score(1)
                match.set_winner(match.player_1)
            elif match_result == "2":
                match.player_2.add_score(1)
                match.set_winner(match.player_2)
            elif match_result == "3":
                match.player_1.add_score(0.5)
                match.player_2.add_score(0.5)

    def build_subsequent_round(self, players_list):
        round_ = RoundModel()

        players = list(
            zip(
                sorted(
                    players_list,
                    key=lambda player: (player.score, -player.rank),
                    reverse=True,
                ),
                [False] * len(players_list),
                # indicate if player already in a match
            )
        )

        for i in range(len(players) - 1):
            player_1, already_matched = players[i]
            if already_matched:
                continue
            for j in range(i + 1, len(players)):
                player_2, already_matched = players[j]
                if already_matched or round_.have_already_played(
                        player_1, player_2):
                    continue
                match = MatchModel(player_1, player_2)
                players[i] = (player_1, True)
                players[j] = (player_2, True)
                round_.add_match(match)
                break
        return round_

    def tournament_rounds(self, tournament):
        rounds_list = []
        for rounds in tournament:
            rounds_id = rounds.get("id")
            round = RoundModel.rounds_table.get(doc_id=rounds_id)
            rounds_list.append(round)
        round = "\n".join(map(str, rounds_list))
        MatchView.display(
            round.replace("'", "")
            .replace("}", "")
            .replace("{", "")
            .replace(",", ""))
        return rounds_list

    def tournament_matches(self, rounds):

        matches_list = []
        for round in rounds:
            round_id = round.get("id")
            matches = RoundModel.rounds_table.get(doc_id=round_id)
            for matches in matches.values():
                for matches_number in matches:
                    match_id = matches_number.get("id")
                    match = MatchModel.matches_table.get(doc_id=match_id)
                    matches_list.append(match)
        match = "\n".join(map(str, matches_list))
        MatchView.display(
            match.replace("'", "")
            .replace("}", "")
            .replace("{", "")
            .replace(",", ""))
