import string
letters = string.ascii_lowercase
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return (all([True if letter in sentence.lower() else False for letter in letters]))