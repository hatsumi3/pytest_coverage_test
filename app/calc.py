"""calc """
import time

def calc_difficult_problem(num:int) -> int:
    time.sleep(num)
    return num * 2

def get_number(num:int) -> int:
    ret = 2 * calc_difficult_problem(num)
    return ret