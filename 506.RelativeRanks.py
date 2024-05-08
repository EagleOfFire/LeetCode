class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        scoreSorted = sorted(score, reverse=True)
        answer = []
        for i in range(len(score)):
            for j in range(len(scoreSorted)):
                if score[i] == scoreSorted[j]:
                    if j == 0:
                        answer.append("Gold Medal")
                    elif j == 1:
                        answer.append("Silver Medal")
                    elif j == 2:
                        answer.append("Bronze Medal")
                    else:
                        answer.append(str(j + 1))
        return answer
