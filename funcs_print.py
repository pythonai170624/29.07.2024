# write function that print the sum of 2 numbers.
# the numbers are argument. default value == 0
def sum_two(a: int = 0, b: int = 0) -> None:
    """sum_two print the sum of 2 given numbers
       default value is 0"""
    print(f"{a} + {b} = {a + b}")


# print the diff of 2 numbers
# the numbers are argument. default value == 0
# call the function with (9999, 4444)
# call the function with no parameters
def diff_two(a: int = 0, b: int = 0) -> None:
    """sum_two print the sum of 2 given numbers
       default value is 0"""
    print(f"{a} - {b} = {a - b}")


# print the biggest of 3 number
# the numbers are argument. default value == 0
# call the function with -10, -100, 1
def biggest(a: int = 0, b: int = 0, c: int = 0) -> None:
    """print the biggest of 3 given numbers
       default value is 0"""
    print(f"max of: {a} {b} {c} ==> is: {max(a, b, c)}")


# function that gets a list and print its length
def print_len(list_param: list[int] = []) -> None:
    """print the length of the given list
       default is []"""
    print(f"length of {list_param} ===> is: {len(list_param)}")


# function that gets a list of int
# print the diff between the max and the min
# call the function with [900, 1010, -87, 0, 10_000]
# should print 10_000 - (-87) = 10_087
def diff_max_min(list_param: list[int] = []) -> None:
    """print the diff between max min of the given list
       default is []"""
    if not list_param:
        print("empty list")
        return
    diff: int = max(list_param) - min(list_param)
    print(f"diff max min of {list_param} ==> is: {diff}")


# function that gets 1 string as parameter
# print tail equals head or not
# "radar" --> print: head equals tail
# "mango" --> print: head is not equals tail
# bonus: ignore case sensitive "Radar" --> equals
# try on word radar, apple, level, civic, noon, shalom
def head_tail(word: str) -> None:
    """print if the head of agiven string is equals to it's tail"""
    if word[0].lower() == word[-1].lower():
        print(f"{word} head == tail")
    else:
        print(f"{word} head NOT equals tail")


# function that gets 2 booleans as parameter
# print "the same" if they are the same
# print "different" if they are different
# default False
# True True --> the same
# False True --> different
# True False --> different
# False False --> the same
def the_same(a: bool = False, b: bool = False) -> None:
    """print if 2 given booleans are the same"""
    if a == b:
        print(f"{a} {b} ==> the same")
    else:
        print(f"{a} {b} ==> NOT the same")


# function that gets 2 floats as parameter
# create a list from these 2 floats
# sort the list and print it
def sort_print_float(a: float = 0, b: float = 0) -> None:
    """gets 2 floats put them in a list, sort and print"""
    list_float: list[float] = [a, b]
    list_float.sort()
    print(list_float)


def main():
    # help(sum_two)
    sum_two(10, 159)
    sum_two()
    words: list[str] = ["radar", "apple", \
                        "level", "civic", "noon"]
    for word in words:
        head_tail(word)


if __name__ == "__main__":
    main()
