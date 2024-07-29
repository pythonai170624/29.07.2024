import funcs_return;

x: int = 90

funcs_return.half(x)  # does nothing
half_value: int = funcs_return.half(x)  # store in half_value
print(funcs_return.half(x))  # print

print(half_value)  # 45
print(max(funcs_return.half(120), 61))  # 61
print(max(60, 61))  # 61
print(max(funcs_return.half(120), funcs_return.half(121)))  # 60


print(funcs_return.power3(5))

# create a list of numbers from 1 to 5 of power3
# example-
# result: [1*1*1, 2*2*2, 3*3*3, 4*4*4, 5*5*5]
#         [1, 8, 27, 64, 125]
power3_list = []
for i in range(1, 6):
    power3_list.append(funcs_return.power3(i))
print(power3_list)

power3_list_co = [funcs_return.power3(i) for i in range(1, 6)]
print(power3_list_co)

print("[0, 0, 0, 0]", funcs_return.all_zeros([0, 0, 0, 0]))
print("[0, 0, 0, 1]", funcs_return.all_zeros([0, 0, 0, 1]))