# https://leetcode.com/problems/sorting-the-sentence/description/
class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        word_positions = [s_list[i][-1] for i in range(len(s_list))]
        words = [s_list[i][:-1] for i in range(len(s_list))]
        new_s_list = ['']*(len(s_list)+1)
        index = 0
        for i in word_positions:
            new_s_list[int(i)] = words[index]
            index+=1
        new_s_list.pop(0)
        new_s_list
        new_s = ' '.join(new_s_list)
        return new_s
