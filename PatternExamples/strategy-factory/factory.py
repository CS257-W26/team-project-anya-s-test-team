from strategies import TankStrategy, PowerSweeperStrategy, UltimateWallStrategy

STRATEGIES = {
    "tank": TankStrategy,
    "sweeper": PowerSweeperStrategy,
    "wall": UltimateWallStrategy
    }

def get_strategy(criteria_name):

    # Look up the class in our dictionary
    strategy_class = STRATEGIES.get(criteria_name.lower())
    
    if not strategy_class:
        raise ValueError(f"Unknown criteria: {criteria_name}")
        
    return strategy_class()