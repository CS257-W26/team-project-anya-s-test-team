from states import NoQuarterState, HasQuarterState, SoldState, SoldOutState

class VendingMachine:
    def __init__(self, count):
        self.count = count
        # Set the initial state
        if count > 0:
            self.current_state = NoQuarterState()
        else:
            self.current_state = SoldOutState()

    def set_state(self, state):
        self.current_state = state

    def insert_quarter(self):
        self.current_state.insert_quarter(self)

    def eject_quarter(self):
        self.current_state.eject_quarter(self)

    def turn_crank(self):
        self.current_state.turn_crank(self)
        self.current_state.dispense(self)

    def release_ball(self):
        print("A soda comes rolling out the slot.")
        if self.count > 0:
            self.count -= 1

# Example usage:
if __name__ == "__main__":
    machine = VendingMachine(5)
    machine.insert_quarter()
    machine.turn_crank()
    machine.insert_quarter()
    machine.eject_quarter()
    machine.insert_quarter()
    machine.turn_crank()