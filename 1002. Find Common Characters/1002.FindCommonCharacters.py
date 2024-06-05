class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # Helper function to count character frequencies in a string
        def count_frequencies(word):
            freq = {}
            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            return freq

        # Initialize the common frequency dictionary with the first word
        common_freq = count_frequencies(words[0])

        # Intersect the frequency count with each word's frequency count
        for word in words[1:]:
            current_freq = count_frequencies(word)
            # Update the common frequency dictionary
            for char in list(common_freq.keys()):
                if char in current_freq:
                    common_freq[char] = min(common_freq[char], current_freq[char])
                else:
                    del common_freq[char]

        # Build the result list based on the final common frequency dictionary
        result = []
        for char, count in common_freq.items():
            result.extend([char] * count)

        return result