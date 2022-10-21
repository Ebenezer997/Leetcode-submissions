class OrderedStream:

    def __init__(self, n: int):
        self.container = {}
        self.current = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.container[idKey] = value
        res = []
       
        while self.current in self.container:
            res.append(self.container[self.current])
            self.current += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)