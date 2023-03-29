list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(list_one)):
    list_one[i] *= 2
print(list_one)
list_two = ['a', 'b', 'c']
list_one.append(list_two)
print(list_one)
if 8 in list_one:
    list_one.remove(8)
print(list_one)
list_one.pop()
print(list_one)