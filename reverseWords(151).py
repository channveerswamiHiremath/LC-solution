class Solution(object):
    def reverseWords(self, s):
        cha = list(s)   
        space = []

        for i in range(len(cha)):
            if cha[i] == ' ':
                space.append(i)

        space = [-1] + space + [len(cha)]

        word = []
        for i in range(len(space) - 1):
            left = space[i] + 1
            right = space[i + 1]
            if left < right:  
                word.append("".join(cha[left:right]))

        return " ".join(word[::-1])
