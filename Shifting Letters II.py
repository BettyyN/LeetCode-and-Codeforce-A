class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shiftCount = [0] * n
        total_shifts = 0
        for start, end, direction in shifts:
            if direction == 0:
                shiftCount[start] -= 1
                if end + 1 < n:
                    shiftCount[end + 1] += 1
            elif direction == 1:
                shiftCount[start] += 1
                if end + 1 < n:
                    shiftCount[end + 1] -= 1
        result = []
        for i in range(n):
            total_shifts += shiftCount[i]
            shift = total_shifts % 26  # 26 letters in the English alphabet
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)    
        return ''.join(result)
        
