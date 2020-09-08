puzzle = [
    [0,0,4,5,2,0,0,6,0],
    [0,0,0,0,0,6,3,0,0],
    [0,0,0,7,8,0,0,0,5],
    [8,0,6,2,3,0,4,0,7],
    [0,9,0,8,7,1,0,5,0],
    [7,0,3,0,6,5,8,0,2],
    [2,0,0,0,4,8,0,0,0],
    [0,0,9,6,0,0,0,0,0],
    [0,8,0,0,9,7,2,0,0]
]

def displayBoard(puzzle):
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
    
        for j in range(len(puzzle[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8: # end of row
                print(str(puzzle[i][j]))
            else:
                print(str(puzzle[i][j]) + " ", end="")

displayBoard(puzzle)