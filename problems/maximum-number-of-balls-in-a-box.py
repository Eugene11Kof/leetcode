# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/
import numpy as np
from collections import Counter
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        balls = [i for i in range(lowLimit,highLimit+1)]
        boxes = []
        for i in balls:
            box = np.sum(list(map(int,list(str(i)))))
            boxes.append(box)
        max_box = np.max(list(dict(Counter(boxes)).values()))
        return max_box
