Given_Integer = int(input())

Binary_Of_Given_Integer = bin(Given_Integer)
Binary_Of_Given_Integer = Binary_Of_Given_Integer[2:]


print(max(map(len,Binary_Of_Given_Integer.split('0'))))
