import sys

class MathHelper:

    def find_largest_number_in_list(self, list_with_numbers):
        """
        Finds and returns the largest number in the given list. For an empty list it returns -sys.maxsize -1
        :param list_with_numbers:
        :return: largest number in list, -sys.maxsize -1 for empty list
        """
        max_number = max(list_with_numbers, default=-sys.maxsize-1)
        return max_number


