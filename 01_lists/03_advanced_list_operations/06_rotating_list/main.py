my_list = [1, 2, 3, 4, 5]
n = 2

n = n % len(my_list)
rotated_list = my_list[-n:] + my_list[:-n]

print("Rotated List:", rotated_list)  #Output: [4, 5, 1, 2, 3]