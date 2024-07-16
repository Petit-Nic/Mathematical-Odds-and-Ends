import os.path
import ast

def adding_new_gens(words, gens):
    new_list = []
    for i in words[-1]:
        for j in gens:
            temp=i.copy()
            temp.append(j)
            new_list.append(temp.copy())
            temp[-1]=-j
            new_list.append(temp)
    return new_list

def reducing_new_gens(new_list):
    reduced_list = []
    for item in new_list:
        i = 0
        while i < len(item)-1:
            if item[i] + item[i+1] == 0:
                break
            elif i == len(item) - 2:
                reduced_list.append(item)
                break
            else:
                i += 1

    return reduced_list


def free_group_words(n, k):
    gens = [i for i in range(1,n+1)]
    words = [[0]]
    new_list = []
    for i in gens:
        new_list.append([i])
        new_list.append([-i])
    words.append(new_list)   

    for i in range(2,k+1):
        new_gens = adding_new_gens(words, gens)
        words.append(reducing_new_gens(new_gens))
    
    return words

def one_more_character(words, n):
     gens = [i for i in range(1,n+1)]
     if words == [] :
         return 0
     if words == [0]:
         temp = []
         for j in gens:
            temp.append([j])
            temp.append([-j])
         return temp
     else:
        k = len(words[-1][0])
         
     new_gens = adding_new_gens(words, gens)
     return reducing_new_gens(new_gens)


def write_to_file(n):
    if not os.path.isfile('free_words_on_'+str(n)+'_generators.txt'):
        open('free_words_on_'+str(n)+'_generators.txt', 'a')
    with open('free_words_on_'+str(n)+'_generators.txt', 'r') as f:
        str_words = f.read()
        if str_words == '':
            words = []
        else:
            words = ast.literal_eval(str_words)
        new_words = one_more_character(words, n)
        words.append(new_words)
    with open('free_words_on_'+str(n)+'_generators.txt', 'w') as f:
        f.write(str(words))



words = write_to_file(1)
