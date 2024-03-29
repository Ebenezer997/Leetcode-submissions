class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
#         dic = {}
        
#         for item in items:
#             if item[0] not in dic:
#                 dic[item[0]] = [item[1]]
#             else:
#                 dic[item[0]].append([item[1]])
        
#         final = []
        
#         def avgsort(list):
#             list = sorted(list, reverse = True)
#             return int((sum(list[0:5]/5))
        
#         for item in dic:
#             final.append([item,avgsort(dic[item])])
#         return sorted(final)
        dic = {}
        for item in items:
            if item[0] in dic:
                dic[item[0]].append(item[1])
            else:
                dic[item[0]] = [item[1]]
        
        final = []
        
        def sort_avg(list):
            list  = sorted(list, reverse = True)
            return int((sum(list[0:5])/5))
        
        for item in dic:
            final.append([item, sort_avg(dic[item])])
        return sorted(final)
            
        