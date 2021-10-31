class HitCounter:

    def __init__(self):
        self.database = {}
        

    def hit(self, timestamp: int) -> None:
            if timestamp not in self.database:
                self.database[timestamp] = 1
            else:
                self.database[timestamp] += 1
            
                
            
        

    def getHits(self, timestamp: int) -> int:
        upperbound = timestamp
        lowerbound = timestamp - 300
        count = 0
        for k,v in self.database.items():
            if k>lowerbound and k <=upperbound:
                count +=v
        return count
            
            
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)