class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counter = Counter(words[0])
        for word in words[1:]:
            common_counter &= Counter(word)
        common_characters = list(common_counter.elements())
        return common_characters
