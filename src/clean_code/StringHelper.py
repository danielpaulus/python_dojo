class StringHelper:
    def strings_are_anagrams(self, first_word, second_word):
        """
        Checks if two words are anagram of each other. F.ex.
        Mary and Amry are anagram, as they contain the same letters only in a different order.
        :param first_word:
        :param second_word:
        :return: True if the words are an Anagram, False otherwise
        """
        if type(first_word) is not str or type(second_word) is not str:
            raise TypeError("Not a string")

        if len(first_word) != len(second_word):
            return False

        for letter in first_word.lower():
            if letter not in second_word.lower():
                return False
            return True
