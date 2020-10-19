#------------------------------------ 2D lists --------------------------------------------------------------
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
# print(number_grid[3][0]) # first num is for row and 2nd num is for column

#--------------------------------------Nested For Loop-----------------------------------------------------

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)