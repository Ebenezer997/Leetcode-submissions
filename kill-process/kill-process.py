class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        result = []
        parent = {}

        for c,p in zip(pid,ppid):
            if p in parent:
                parent[p].append(c)
            else:
                parent[p] = [c]

        q = collections.deque([kill])
        while q:
            for _ in range(len(q)):
                process = q.popleft()
                result.append(process)

                if process in parent:
                    q.extend(parent[process])  
        return result
        