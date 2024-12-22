tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*tuple_list)

list1 = list(list1)
list2 = list(list2)

print(list1)  #output: [1, 2, 3]
print(list2)   #output: ['a', 'b', 'c']