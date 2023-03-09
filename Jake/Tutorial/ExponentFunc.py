def raisePower(baseNum, powNum):
    result = 1
    for index in range(powNum):
        result = result * baseNum
        return result

print(raisePower(2,3))

number_grid = [
    [1, 2, 3],
    [6, 5, 3],
    [1],
    [1, 4, 6, 8]
]
print(number_grid[0][0])
print(number_grid[0][2])

for row in number_grid:
    for col in row:
        print(col)
