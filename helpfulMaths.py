board_line = input()
num_arr = board_line.split('+')
num_arr.sort()
result = "+".join(num_arr)
print(result)