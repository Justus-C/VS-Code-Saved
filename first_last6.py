#February 19, 2020

from typing import List
def first_last_6(list: List[int]) -> bool:
    is_first_last_6 = False
    if list[0] == 6 or list[-1] == 6:
        is_first_last_6 == True
    return is_first_last_6
