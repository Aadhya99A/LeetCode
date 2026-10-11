class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        strk = ""
        for word in words:
            if word == word[::-1]:
                strk += word
                break
        return strk