# here's the question
# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175


yeet = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


def add_them(arr):

    return_number = 0

    for x in arr:
        return_number += min(x)
    
    return return_number

print(add_them(yeet))
        
