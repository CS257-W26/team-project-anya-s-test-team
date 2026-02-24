from strategies import TankStrategy, PowerSweeperStrategy, UltimateWallStrategy

class RankingStrategyFactory:
    """
    Centralized location for creating ranking strategies.
    This keeps the Web Controller clean.
    """
    _strategies = {
        "tank": TankStrategy,
        "sweeper": PowerSweeperStrategy,
        "wall": UltimateWallStrategy
    }

    @staticmethod
    def get_strategy(criteria_name):
        # Look up the class in our dictionary
        strategy_class = RankingStrategyFactory._strategies.get(criteria_name.lower())
        
        if not strategy_class:
            raise ValueError(f"Unknown criteria: {criteria_name}")
            
        return strategy_class()