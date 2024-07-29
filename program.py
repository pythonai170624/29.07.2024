import funcs_print

# x: int = input("enter a:")
# y: int = input("enter b:")
# demo1.sum_two(x, y)
funcs_print.sum_two(5, 12)
funcs_print.sum_two()
funcs_print.diff_two(9999, 4444)
funcs_print.diff_two()
funcs_print.biggest(-10, -100, 1)
funcs_print.print_len([8, 10, 200, -300])
funcs_print.diff_max_min([900, 1010, -87, 0, 10_000])
funcs_print.diff_max_min()

funcs_print.head_tail("radar")
funcs_print.head_tail("mango")
words: list[str] = ["radar", "apple", \
                    "level", "civic", "noon"]
for word in words:
    funcs_print.head_tail(word)

# for index, word in enumerate(words):
#     demo1.head_tail(word)

# run in loop of list:
# send each word to the function

# opt = [[f1, f2] for f1 in [True, False] for f2 in [True, False]]
# print(opt)
opt_ = [[True, True], [False, True], [True, False], [False, False]]
for opt_in in opt_:
    funcs_print.the_same(opt_in[0], opt_in[1])

print('goodbye!')

# numbers: list[int] = [1,4,6,200]
# for number in numbers:
#     print(number)