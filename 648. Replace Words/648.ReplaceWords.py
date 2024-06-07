class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = ""
        words = sentence.split(" ")
        for i in range(len(words)):
            for definition in dictionary:
                if words[i].startswith(definition):
                    words[i] = definition
        for word in words:
            ans += word + " "
        ans = ans[:-1]
        return ans