class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        eml = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                eml.append("FizzBuzz")
            elif i%3 == 0:
                eml.append("Fizz")
            elif i%5 == 0:
                eml.append("Buzz")
            else:
                eml.append(str(i))
        return eml