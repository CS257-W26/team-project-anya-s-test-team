class Coffee:
    def get_cost(self): 
        return 2.0

class MilkDecorator:
    def __init__(self, component):
        self._component = component
    def get_cost(self):
        return self._component.get_cost() + 0.5

class SugarDecorator:
    def __init__(self, component):
        self._component = component
    def get_cost(self):
        return self._component.get_cost() + 0.2

# Usage: Mix and match dynamically at runtime!
my_order = SugarDecorator(MilkDecorator(Coffee()))
print(f"Total: ${my_order.get_cost()}")