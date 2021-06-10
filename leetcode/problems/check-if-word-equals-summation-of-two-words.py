class Solution(object):
    def calculateWordScore(self, word):
        char_scores = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        score = ''
        for char in word:
          score = score + str(char_scores.index(char))
        return score


    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """

        return (int(self.calculateWordScore(firstWord)) + int(self.calculateWordScore(secondWord))) == int(self.calculateWordScore(targetWord))
