from abc import ABC, abstractmethod

# 1. The Strategy Interface
class RankingStrategy(ABC):
    @abstractmethod
    def get_formula(self):
        pass

# 2. Concrete Strategies
class PowerSweeperStrategy(RankingStrategy):
    def get_formula(self):
        return "(speed * (CASE \
                WHEN attack > sp_attack \
                THEN attack ELSE sp_attack END))"

class UltimateWallStrategy(RankingStrategy):
    def get_formula(self):
        return "(hp * (defense + sp_defense))"

class TankStrategy(RankingStrategy):
    def get_formula(self):
        return "(hp * defense)"
    
