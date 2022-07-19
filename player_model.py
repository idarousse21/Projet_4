class PlayersModel:
    def __init__(self, last_name, first_name, date_of_birth, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.full_name = f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return str({
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking,
        })
