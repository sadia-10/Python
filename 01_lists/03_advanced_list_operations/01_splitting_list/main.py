numbers = [1, 2, 3, 4, 5, 6, 7, 8]
mid_index = len(numbers) // 2

first_half = numbers[:mid_index]
second_half = numbers[mid_index:]

print("First Half:", first_half)        #output: First Half: [1, 2, 3, 4]
print("Second Half:", second_half)      #output: Second Half: [5, 6, 7, 8]