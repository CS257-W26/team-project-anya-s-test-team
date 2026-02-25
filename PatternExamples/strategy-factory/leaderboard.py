
import factory
class LeaderBoard:
    def __init__(self, strategy):
        self._strategy = strategy
        #self.ds = DataSource()

    def set_strategy(self, strategy):
        self._strategy = strategy

    def fetch_leaders(self):
        formula = self._strategy.get_formula()
        print("Going to ask DataSource for", formula)
        #return ds.get_top_ten(formula)
        

# stand in for flask route handler
def get_leaderboard(criteria):
    try:
        strategy = factory.get_strategy(criteria)
        leaderboard = LeaderBoard(strategy)
        return leaderboard.fetch_leaders()
    except ValueError:
        return "Leaderboard type not found", 404

if __name__ == "__main__":
    # Example usage of get_leaderboard function
    print(get_leaderboard("tank"))