class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dis = len(colors)
        md = []
        for i in range(dis):
            for j in range(i +1, dis):
                if colors[i] != colors[j]:
                    md.append(abs(i - j))
        return max(md)