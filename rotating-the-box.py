# https://leetcode.com/problems/rotating-the-box/description/
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        new_box = []
        global_index = 0
        for i in box:
            box0 = box[global_index]
            rbox0 = box0[::-1]
            new_rbox0 = [-1]*(len(box0))
            index = 0
            lowest_empty_index = 0
            for i in rbox0:
                if i == '#':
                    if index == lowest_empty_index:
                        # rbox0[index] = 1
                        lowest_empty_index += 1
                    else:
                        rbox0[index] = '.'
                        rbox0[lowest_empty_index] = '#'
                        lowest_empty_index += 1
                elif i == '*':
                    lowest_empty_index = index + 1
                else:
                    rbox0[index] = i
                index+=1
            box0 = rbox0[::-1]
            new_box.append(box0)
            global_index+=1
        new_box2 = [['' for i in range(len(new_box))] for i in range(len(new_box[0]))]
        for i in range(len(new_box[0])):
            for j in range(len(new_box)):
                new_box2[i][j] = new_box[len(new_box)-1-j][i]
        return new_box2
