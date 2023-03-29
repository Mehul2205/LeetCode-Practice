class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if(len(satisfaction) ==0):
            return 0
        abc = sorted(satisfaction)

        sum1 = sum(abc)
        if sum1 < 0:
            return self.maxSatisfaction(abc[1:])
        else:
            return sum([(i+1)*a for i,a in enumerate(abc)])
        