import random
from itertools import product, permutations
import time
import numpy as np

start_time = time.time()

def generate(letter_array):
    #D E Y N R O
    solution = [[None,None, None, None],[None,None, None, None], [None,None, None, None, None]]
    P = [0, None, None, None, None]
    elem_array = [0,0,0,0]
    #first = list(permutations([9,8,7,6,5,4,3,2,1,0], 2))
    #random.shuffle(first)

    first = list(product([9,8,7,6,5,4,3,2,1,0], [9,8,7,6,5,4,3,2,1,0]) )
    random.shuffle(first)
    i = 3; 

    while(elem_array[0] < len(first)):
     while(elem_array[3-i] < len(first)):
          solution[0][i] = first[elem_array[3-i]][0]
          solution[1][i] = first[elem_array[3-i]][1]
          solution_body = body(P,solution,i, letter_array)
          if(solution_body != False):
                [solution, P] =  solution_body
                if(i == 0):
                  if( int("".join(map(str, solution[0]))) + int("".join(map(str, solution[1]))) == int("".join(map(str, solution[2])))):
                        return solution
                  solution, P = clear(i,solution,P)
                  i+=1
                i-=1
          solution, P = clear(i,solution,P)
          elem_array[3-i] += 1
     if(i != 3):
        elem_array[3-i] = 0
        i+=1
        solution, P = clear(i,solution,P)
        elem_array[3-i] += 1
    return None


def clear(i,solution,P):
    for k in range(i+1):
        P[4-k] = None
        for j in range(3):
            solution[j][k] = None
    solution[2][i+1] = None
    return solution, P


def sucet(a,b,c,d,e):
    if(e == None):
      e = (a + b + c)//10
    else:
        if(e != (a + b + c)//10):
            return False
    if(d == None):
         d = (a + b + c)%10
    else:
        if(d != (a + b + c)%10):
            return False
    return e, d

def dif(i, solution, letter_array):
    for j1 in range(3):
        for g1 in range(4):
           for j2 in range(3):
              for g2 in range(4):

               if(letter_array[j1][g1] == letter_array[j2][g2]):
                    if(solution[j2][g2] == None):
                       solution[j2][g2] = solution[j1][g1]
                    elif(solution[j1][g1] == None): 
                        solution[j1][g1] = solution[j2][g2]
                    else:
                       if(solution[j1][g1] != solution[j2][g2]):   
                          return False
               else:
                    if(solution[j1][g1] == solution[j2][g2] and solution[j1][g1] != None):
                        return False 

               if(j1 == 2):
                  if(letter_array[j1][g1 + 1] == letter_array[j2][g2]):
                    if(solution[j1][g1 + 1] == None):
                        solution[j1][g1 + 1] = solution[j2][g2]
                    elif(solution[j2][g2] == None):
                        solution[j2][g2] = solution[j1][g1 + 1]
                    else:
                        if(solution[j1][g1 + 1] != solution[j2][g2]):   
                           return False
                  else:
                      if(solution[j1][g1 + 1] == solution[j2][g2] and solution[j2][g2] != None):
                        return False

    return solution

def body(P,solution,i, letter_array):
       if(i == 0):
           if(solution[0][0] == 0 or solution[1][0] == 0):
               return False
       exa_sucet = sucet(P[3-i], solution[0][i], solution[1][i], solution[2][i+1], P[4-i])
       if(exa_sucet != False):  
             P[4-i], solution[2][i+1] = exa_sucet
             if(i == 0):
                 solution[2][0] = P[4]
                 if(solution[2][0] == False):
                     return False
             diferens = dif(i, solution, letter_array) 
             if(diferens != False):
                solution = diferens
                return [solution, P]
       return False

print(generate([['S','E','N','D'],['M','O','R','E'],['M','O','N','E','Y']]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print(generate([['S','E','N','D'],['M','O','R','E'],['M','O','N','E','Y']]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print(generate([['S','E','N','D'],['M','O','R','E'],['M','O','N','E','Y']]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print(generate([['S','E','N','D'],['M','O','R','E'],['M','O','N','E','Y']]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print(generate([['S','E','N','D'],['M','O','R','E'],['M','O','N','E','Y']]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print(generate([['B','A','S','E'],['B','A','L','L'],['G','A','M','E','S']]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print(generate([['L','O','G','I'],['L','O','G','I'],['P','R','O','L','O']]))
print("--- %s seconds ---" % (time.time() - start_time)) 
start_time = time.time()