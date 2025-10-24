from project.indexing import Indexing


class Trainer(Indexing):

    def __init__(self, name: str):
        self.name = name
        self.id = self.set_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
