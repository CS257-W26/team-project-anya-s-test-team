from vending_abc import VendingState

class NoQuarterState(VendingState):
    def insert_quarter(self, machine):
        print("You inserted a quarter.")
        machine.set_state(HasQuarterState())

    def eject_quarter(self, machine):
        print("You haven't inserted a quarter.")

    def turn_crank(self, machine):
        print("You turned, but there's no quarter.")

    def dispense(self, machine):
        print("You need to pay first.")

class HasQuarterState(VendingState):
    def insert_quarter(self, machine):
        print("You can't insert another quarter.")

    def eject_quarter(self, machine):
        print("Quarter returned.")
        machine.set_state(NoQuarterState())

    def turn_crank(self, machine):
        print("You turned...")
        machine.set_state(SoldState())
    def dispense(self, machine):
        print("No soda dispensed.")

class SoldState(VendingState):
    def insert_quarter(self, machine):
        print("Please wait, we're already giving you a soda.")

    def eject_quarter(self, machine):
        print("Sorry, you already turned the crank.")

    def turn_crank(self, machine):
        print("Turning twice doesn't get you two sodas!")

    def dispense(self, machine):
        machine.release_ball()
        if machine.count > 0:
            machine.set_state(NoQuarterState())
        else:
            print("Oops, out of sodas!")
            machine.set_state(SoldOutState())
class SoldOutState(VendingState):
    def insert_quarter(self, machine):
        print("You can't insert a quarter, the machine is sold out.")

    def eject_quarter(self, machine):
        print("You can't eject, you haven't inserted a quarter.")

    def turn_crank(self, machine):
        print("You turned, but there are no sodas.")

    def dispense(self, machine):
        print("No soda dispensed.")