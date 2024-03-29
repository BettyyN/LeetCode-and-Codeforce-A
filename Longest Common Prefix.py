class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chlist = []
        pntr = 0
        if len(strs) == 1:
            return strs[0]
        else:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if pntr >= len(strs[j]) or strs[0][pntr] != strs[j][pntr]:
                        return ''.join(chlist)
                chlist.append(strs[0][pntr])
                pntr += 1
            return ''.join(chlist)
