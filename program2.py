import demo2;

x: int = 90

demo2.half(x)  # does nothing
half_value: int = demo2.half(x)  # store in half_value
print(demo2.half(x))  # print

print(half_value)  # 45
print(max(demo2.half(120), 61))  # 61
print(max(60, 61))  # 61
print(max(demo2.half(120), demo2.half(121)))  # 60


print(demo2.power3(5))

# create a list of numbers from 1 to 5 of power3
# example-
# result: [1*1*1, 2*2*2, 3*3*3, 4*4*4, 5*5*5]
#         [1, 8, 27, 64, 125]
power3_list = []
for i in range(1, 6):
    power3_list.append(demo2.power3(i))
print(power3_list)

power3_list_co = [demo2.power3(i) for i in range(1, 6)]
print(power3_list_co)

print("[0, 0, 0, 0]", demo2.all_zeros([0, 0, 0, 0]))
print("[0, 0, 0, 1]", demo2.all_zeros([0, 0, 0, 1]))