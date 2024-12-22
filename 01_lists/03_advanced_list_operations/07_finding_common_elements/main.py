list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common_elements = list(set(list1) & set(list2))
print("Common Elements:", common_elements)  #Output:Common Elements: [3, 4]
