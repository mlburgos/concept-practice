# Write a class TempTracker with these methods:
#
# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean ↴ of all temps we've seen so far
# get_mode()—returns a mode ↴ of all temps we've seen so far


class TempTracker(object):
    """
    """
    def __init__(self):
        self.temps_dict = {}
        self.maxi = 0
        self.mini = 110
        self.highest_freq = 0
        self.count = 0
        self.total = 0

    def insert(self, temp):
        """Records a new temperature"""
        self.temps_dict[temp] = self.temps_dict.get(temp, 0) + 1

        self.count += 1
        self.total += temp
        self.highest_freq = max(self.temps_dict[temp], self.highest_freq)
        self.maxi = max(self.maxi, temp)
        self.mini = min(self.mini, temp)

    def get_max(self):
        """returns the highest temp we've seen so far"""
        return self.maxi

    def get_min(self):
        """returns the lowest temp we've seen so far"""
        return self.mini

    def get_mean(self):
        """returns the mean of all temps we've seen so far"""
        return float(self.total)/self.count

    def get_mode(self):
        """returns a mode of all temps we've seen so far"""
        modes = []
        for temp, freq in self.temps_dict.items():
            if freq == self.highest_freq:
                modes.append(temp)

        return modes

