perso = [
    {"nom": "pop", "ranking": 1, "score": 0},
    {"nom": "bob", "ranking": 2, "score": 0},
    {"nom": "po", "ranking": 3, "score": 0},
    {"nom": "pp", "ranking": 4, "score": 0},
    {"nom": "popi", "ranking": 5, "score": 0},
    {"nom": "popo", "ranking": 6, "score": 0},
    {"nom": "popz", "ranking": 7, "score": 0},
    {"nom": "popr", "ranking": 8, "score": 0},
]
group_top_ranking = []
group_bottom_ranking = []
# def add_player_groupe(self):
p = sorted(perso, key=lambda pers: pers["ranking"])
for player in perso[:4]:
    group_top_ranking.append(player)
for player in perso[-4:]:
    group_bottom_ranking.append(player)

# group_1 = perso[: int(len(perso) / 2)]
# group_2 = perso[int(len(perso) / 2) :][::-1]
print(group_bottom_ranking)
