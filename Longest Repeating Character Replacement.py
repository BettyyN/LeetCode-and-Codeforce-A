class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        start = 0
        count_map = [0] * 26  # Assuming only uppercase English characters
        for end in range(len(s)):
            index = ord(s[end]) - ord('A')
            count_map[index] += 1
            max_count = max(max_count, count_map[index])
            while end - start + 1 - max_count > k:
                count_map[ord(s[start]) - ord('A')] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length
                
