class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float((target-p) / s) for p,s in sorted(zip(position,speed))]
        cur = 0
        flt = 0
        for i in time[::-1]:
            if i > cur:
                cur = i
                flt+=1
        return flt
