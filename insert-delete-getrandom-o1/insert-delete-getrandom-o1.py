class RandomizedSet:
    def __init__(self):
        self.database = {}
        

    def insert(self, val: int) -> bool:
        if val in self.database:
            return False
        else:
            self.database[val] = val
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.database:
                self.database.pop(val)
                return True
        else:
            return False
        
        

    def getRandom(self) -> int:
        a = random.choice(list(self.database))
        
        return a
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()