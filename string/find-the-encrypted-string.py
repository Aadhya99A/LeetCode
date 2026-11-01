from collections import deque
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        rot = len(s) - k%len(s)
        dq = deque(list(s))
        dq.rotate(rot)
        ret = ""
        for i in dq:
            ret += i
        return ret