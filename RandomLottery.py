from random import sample
from typing import List


class Lottery:
    def __init__(self):
        pass

    @staticmethod
    def lottery_result() -> List[int]:
        """
        Randomly generate the lottery result from 1 to 50
        :return: list of 10 lottery balls  from 1 to 50 in ascending order
        """
        return sorted(sample(range(1, 51), 10))

    @staticmethod
    def result_is_valid(lottery_results: List[int]) -> bool:
        """
        Test cases to check if the lottery result is valid
        :param lottery_results: list of the lottery result
        :return: True if the result is valid False if the result isn't valid
        """
        max_num = max(lottery_results)
        min_num = min(lottery_results)
        result_set = set(lottery_results)

        if max_num > 50 or min_num < 1 or len(result_set) != 10:
            return False
        return True


if __name__ == "__main__":
    # Demo result
    lottery_result = Lottery.lottery_result()
    Lottery.result_is_valid(lottery_result)