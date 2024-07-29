import demo1

# x: int = input("enter a:")
# y: int = input("enter b:")
# demo1.sum_two(x, y)
demo1.sum_two(5, 12)
demo1.sum_two()
demo1.diff_two(9999, 4444)
demo1.diff_two()
demo1.biggest(-10, -100, 1)
demo1.print_len([8, 10, 200, -300])
demo1.diff_max_min([900, 1010, -87, 0, 10_000])
demo1.diff_max_min()

demo1.head_tail("radar")
demo1.head_tail("mango")
words: list[str] = ["radar", "apple", \
                    "level", "civic", "noon"]
for word in words:
    demo1.head_tail(word)

# for index, word in enumerate(words):
#     demo1.head_tail(word)

# run in loop of list:
# send each word to the function

# opt = [[f1, f2] for f1 in [True, False] for f2 in [True, False]]
# print(opt)
opt_ = [[True, True], [False, True], [True, False], [False, False]]
for opt_in in opt_:
    demo1.the_same(opt_in[0], opt_in[1])

print('goodbye!')

# numbers: list[int] = [1,4,6,200]
# for number in numbers:
#     print(number)