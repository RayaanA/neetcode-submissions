class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float((target-p)/s) for p,s in sorted(zip(position,speed))]
        flt = 0
        curr = 0
        for i in time[::-1]:
            if i > curr:
                curr = i
                flt+=1
        return flt