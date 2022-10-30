list_6 = [i**2 * -1 if i % 2 == 0 else i**2 for i in range(1, 11)]
list_7 = [x for y in range(2,13) for x in range(3,13,y)]
print(list_7)