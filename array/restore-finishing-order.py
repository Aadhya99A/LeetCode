class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ret = []
        for i in order:
            if i in friends:
                ret.append(i)
        return ret