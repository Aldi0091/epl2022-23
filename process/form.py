import csv


class Data:
    @classmethod
    def all_games(cls):
        all_data = tuple()
        with open("process/E0.csv", "r") as csvfile:
            lines = csv.reader(csvfile, delimiter=",")
            for data in lines:
                all_data += ([data[i] for i in range(3, 8)],)
        return all_data

    @classmethod
    def team_value(cls):
        sett = set()
        for item in cls.all_games():
            sett.add(item[0])

        return sett
