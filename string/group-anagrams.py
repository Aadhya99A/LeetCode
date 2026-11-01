class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}
        for i in strs:
            str_id = tuple(sorted(i))
            if str_id not in seen:
                seen[str_id] = [i]
            else:
                seen[str_id].append(i)
        print(seen)
        return list(seen.values())