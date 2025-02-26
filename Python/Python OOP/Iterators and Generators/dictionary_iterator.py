class dictionary_iter:

    def __init__(self, dict):
        self.dict = list(dict.items())
        self.last_idx=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.last_idx+=1
        if self.last_idx>=len(self.dict):
            raise StopIteration()
        return self.dict[self.last_idx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
