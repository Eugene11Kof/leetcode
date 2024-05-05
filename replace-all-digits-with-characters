# https://leetcode.com/problems/replace-all-digits-with-characters/description/
class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabet = list(string.ascii_lowercase)
        s_list= list(s)
        s_new = s_list.copy()
        index=0
        for i in s_list:
            if i in alphabet:
                s_new[index] = i
                last_symbol = i
            else: 
                s_new[index] = last_symbol
                s_new[index] =  alphabet[alphabet.index(last_symbol) + int(i)]
                last_symbol = i
            index+=1
        s_new_str = ''.join(s_new)
        return s_new_str
