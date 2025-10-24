from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    valid_computers = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):

        if type_computer not in self.valid_computers:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = self.valid_computers[type_computer](manufacturer, model)
        configured_computer = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return configured_computer

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."

        else:
            raise Exception("Sorry, we don't have a computer for you.")
