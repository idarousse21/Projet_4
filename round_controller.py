from round_model import MatchModel, RoundModel
from round_view import MatchView


class ControllerRound:
    def __init__(self):
        self.match_view = MatchView()

    def build_first_round(self, players_list):
        round_ = RoundModel()
        players = sorted(
            players_list,
            key=lambda player: player.ranking,
        )
        group_top_ranking = []
        group_bottom_ranking = []
        for player in players[: int(len(players) / 2)]:
            group_top_ranking.append(player)
        for player in players[-int(len(players) / 2) :][::-1]:
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
            match_result = self.match_view.end_match(match.player_1, match.player_2)
            if match_result == "1":
                match.player_1.add_score(1)
                match.set_winner(match.player_1)
            elif match_result == "2":
                match.player_2.add_score(1)
                match.set_winner(match.player_2)
            else:
                match.player_1.add_score(0.5)
                match.player_2.add_score(0.5)

    def build_subsequent_round(self, players_list):
        round_ = RoundModel()
        players = list(
            zip(
                sorted(
                    players_list,
                    key=lambda player: (player.score, -player.ranking),
                    reverse=True,
                ),
                [False] * len(players_list),
            )
        )

        for i in range(len(players)):
            player_1, already_matched = players[i]
            if already_matched:
                continue
            for j in range(i + 1, len(players)):
                player_2, already_matched = players[j]
                print(player_1, player_2)
                if already_matched or round_.have_already_played(player_1, player_2):
                    continue
                match = MatchModel(player_1, player_2)
                round_.add_match(match)
        print(round_.matches)
        return round_
