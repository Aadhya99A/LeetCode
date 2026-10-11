class Solution:
    def isNumber(self, s: str) -> bool:
        if any([s=="inf", s == "-inf", s == "+inf", s == "Infinity", s == "-Infinity", s == "+Infinity", s == "infinity", s == "-infinity", s == "+infinity", s == "nan", s == "NaN"]):
            return False
        try:
            k = float(s)
            return True
        except ValueError:
            return False