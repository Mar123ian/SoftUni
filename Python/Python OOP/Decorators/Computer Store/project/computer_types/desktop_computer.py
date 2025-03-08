from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    processors={"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
    allowed_ram={2:1,4:2,8:3,16:4,32:5,64:6,128:7}
    def configure_computer(self, processor: str, ram: int):

        if processor not in self.processors:
            raise ValueError(f"{ processor } is not compatible with desktop computer { self.manufacturer} { self.model}!")

        if ram not in self.allowed_ram:
            raise ValueError(f"{ ram }GB RAM is not compatible with desktop computer { self.manufacturer} { self.model}!")

        self.processor=processor
        self.ram=ram
        self.price=self.processors[processor]+100*self.allowed_ram[ram]

        return f"Created { self.manufacturer} { self.model} with { self.processor } and { ram }GB RAM for { self.price }$."

