import itertools


class TournamentModel:
    def __init__(
        self,
        tournament_name,
        tournament_venue,
        tournament_start_date,
        tournament_end_date,
    ):
        self.tournament_name = tournament_name
        self.tournament_venue = tournament_venue
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.number_turns = 4
        self.players_list = []
        self.group_top_ranking = []
        self.group_bottom_ranking = []
        self.match_list = []
        self.melange = []
        self.round1 = []
        self.round2 = []

    def __repr__(self):
        return str(
            {
                "tournament_name": self.tournament_name,
                "tournament_venue": self.tournament_venue,
                "tournament_start_date": self.tournament_start_date,
                "tournament_end_date": self.tournament_end_date,
                "number_turns": self.number_turns,
            }
        )

    def add_player(self, player):
        self.players_list.append(player)

    def add_player_groupe(self):
        p = sorted(self.players_list, key=lambda players_list: players_list.ranking)
        for player in p[:2]:
            self.group_top_ranking.append(player)
        for player in p[-2:]:
            self.group_bottom_ranking.append(player)

    def round_1(self):
        self.group_bottom_ranking = sorted(
            self.group_bottom_ranking, key=lambda player: player.ranking, reverse=True
        )
        for player_1, player_2 in itertools.zip_longest(
            self.group_top_ranking, self.group_bottom_ranking
        ):
            self.round1.append((player_1, player_2))

    def game_round(self):
        # match_list.append(round_now)
        for i in self.round1:
            print(i)
            # self.match_list.append(i)
            p = input(str(f"résultat match {i} (nom + win, draw): "))
            print(i[0].last_name)
            if p == i[0].last_name + " win":
                print(str(i[0].last_name + " a gagner!"))
                i[0].update(i[0].score + 1)
            elif p == str(i[1].last_name + " win"):
                print(str(i[1].last_name + " a gagner!"))
                i[1].update(i[1].score + 1)
            elif p == str("draw"):
                print("match nul")
                i[0].update(i[0].score : 0.5)
                i[1].update(i[1].score + 0.5)
            self.melange.extend(i)

        self.melange = sorted(self.melange, key=TournamentModel.tri_list, reverse=True)

    def tri_list(x):
        return [x["score"], -x["ranking"]]
