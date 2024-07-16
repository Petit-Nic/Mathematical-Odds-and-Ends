import math
import random
import matplotlib.pyplot as plt

def vertical(carpet, i, j):
    return 2*carpet[j-1][i]-carpet[j-2][i]

def horizontal(row, i, j):
    return 2*row[-1] - row[-2]

def create_fringe(p, number_of_permutations, rand):
    base = [i for i in range(p)]
    j = 0
    fringe = []
    for j in range(number_of_permutations):
        temp_base = base.copy()
        for i in range(p):
            if rand:
                color = temp_base.pop(math.floor((p-i-1)*(random.random())))
            else: 
                color = temp_base.pop(0)
            fringe.append(color)
    return fringe


def carpet_matrix(p, size, rand_perm=False):
    fringe1 = create_fringe(p, size, rand_perm)
    fringe2 = create_fringe(p, size, rand_perm)
    print(fringe1)
    print(fringe2)
    padding = fringe1.copy()
    padding.insert(0,0)
    padding.insert(0,0)
    carpet = [padding, padding]

    for j in range(len(fringe2)):
        if j % 2 == 0:
            direction = 'v'
        else: 
            direction = 'h'
        
        row = [fringe2[j], fringe2[j]]
        i=0
        while i < len(fringe1):            
            i += 1
            match direction:
                case 'h':
                    row.append(horizontal(row, i+1, j+2) % p)
                    direction = 'v'
                case 'v': 
                    row.append(vertical(carpet, i+1, j+2) % p)
                    direction = 'h'
        carpet.append(row)

    return carpet

carpet = carpet_matrix(3,3 ** 5, True)
plt.matshow(carpet)

plt.show()


