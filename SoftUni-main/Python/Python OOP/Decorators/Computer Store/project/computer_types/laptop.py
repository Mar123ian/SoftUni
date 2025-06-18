from project.computer_types.computer import Computer


class Laptop(Computer):

    processors={"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
    allowed_ram={2:1,4:2,8:3,16:4,32:5,64:6}
    def configure_computer(self, processor: str, ram: int):

        if processor not in self.processors:
            raise ValueError(f"{ processor } is not compatible with laptop { self.manufacturer} { self.model}!")

        if ram not in self.allowed_ram:
            raise ValueError(f"{ ram }GB RAM is not compatible with laptop { self.manufacturer} { self.model}!")

        self.processor=processor
        self.ram=ram
        self.price=self.processors[processor]+100*self.allowed_ram[ram]

        return f"Created { self.manufacturer} { self.model} with { self.processor } and { ram }GB RAM for { self.price }$."

