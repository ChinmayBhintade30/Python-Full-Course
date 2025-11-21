matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


#this is how we implement the matrix in python using 2D lists in the form of 2D lists

# print(matrix[0][1])
# we get 2 as the anwer which is 0th row and 1st column - as indexing starts from 0 
#In this matrix we have row - 0,1,2 and col - 0,1,2

#we can interate the matrix by using while loop --> using only row and item in rows

for row in matrix:
    for item in row:
        print(item )


"""
all the elements in matrix 
1
2
3
4
5
6
7
8
9
"""