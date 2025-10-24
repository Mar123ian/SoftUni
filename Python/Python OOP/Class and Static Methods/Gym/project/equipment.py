from project.indexing import Indexing


class Equipment(Indexing):

    def __init__(self, name: str):
        self.name = name
        self.id = self.set_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
