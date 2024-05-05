# https://leetcode.com/problems/second-largest-digit-in-a-string/description/
class Solution:
    def secondHighest(self, x: str) -> int:
        any_digits = [i for i in range (0,10)]
        any_digits = list(map(str,any_digits))
        our_digits = []
        for i in x:
            if i in any_digits and i not in our_digits:
                our_digits.append(i)
        our_digits = list(map(int,our_digits))    
        our_digits_sorted = sorted(our_digits)[::-1]
        if len(our_digits_sorted) > 1:
            # answer = f'The second lastgest digit is {our_digits_sorted[1]}'
            answer = our_digits_sorted[1]
        else:
            # answer = 'There is not second largest digit'
            answer = -1
        return answer

        
