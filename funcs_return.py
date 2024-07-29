# write a function that gets a number and
# returns half of it (as int)
def half(x: int = 0) -> int:
    """returns half"""
    if x == None:
        return None
    return x // 2


# write a function that gets a number
#  and returns the number power 3
#  2 power 3 ==    2*2*2 == 8
# 10 power 3 == 10*10*10 == 1000
def power3(x: int = 0) -> int:
    """returns power3"""
    result: int = x ** 3
    return result


# write a function that gets a list
# if all the values in the list are not zero
# return string "non-zero" else return "with zero"
# hint: any
def all_zeros(list_numbers: list[int] = []) -> str:
    if not any(list_numbers):
        return "all zeros"
    else:
        return "not all zeros"
