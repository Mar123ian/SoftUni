class Indexing:
    id=1
    @classmethod
    def set_id(cls):

        cls.id+=1
        return cls.id-1

    @classmethod
    def get_next_id(cls):
        return cls.id