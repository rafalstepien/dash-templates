import pandas as pd
from collections import defaultdict, OrderedDict


class Data:

    def __init__(self, path, sep):
        self.content = pd.read_csv(path, sep=sep)
        self.file = path.split("/")[-1]

    def __repr__(self):
        return "Data({})".format(self.file)

    def head(self, n):
        print(self.content.head(n))

    def get_medium_length_subset(self):
        mediums = pd.DataFrame(columns=list(self.content))
        for id, row in self.content.iterrows():
            # if 1300 < int(row['length']) < 1600:
            if int(row['length']) == 1302:
                mediums = mediums.append(row)
        return mediums

    def get_histogram_data(self):
        lengths_occurrences = defaultdict(list)
        for id, row in self.content.iterrows():
            lengths_occurrences[row['length']].append(row['target_id'])
        lengths_occurrences = {lengths: len(occurrences) for lengths, occurrences in lengths_occurrences.items()}
        lengths_occurrences = OrderedDict(sorted(lengths_occurrences.items(), key=lambda t: t[0]))
        x = list(lengths_occurrences.keys())
        y = list(lengths_occurrences.values())
        return x, y
