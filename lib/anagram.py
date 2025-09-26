# your code goes here!
class Anagram:
    def __init__(self, word):
        # store the base word in lowercase
        self.word = word.lower()

    def match(self, words):
        """
        Return all words from the list that are anagrams of self.word.
        """
        sorted_word = sorted(self.word)
        matches = []

        for w in words:
            if w.lower() != self.word and sorted(w.lower()) == sorted_word:
                matches.append(w)

        return matches
