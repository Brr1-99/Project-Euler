"""
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""

import itertools, copy

def limit_numbers(inf: int, sup: int, coef: list[int]) -> tuple[list[int], list[str]]:
    numbers = []
    i = 19
    while i < 141: 
        number = int(i*(coef[0]*i - coef[1])/coef[2])
        if number > sup:
            break
        if number > inf and str(number)[-2] != '0':
            numbers.append(number)
        i+= 1
    return numbers


def match_cycle(num1: int, num2: int) -> bool:
    result = False
    s1 = str(num1)
    s2 = str(num2)
    if (s1[2:4] == s2[0:2]):
        result = True
    return result

def find_chains(num: int, match: list[int], sets: list[int]) -> bool: 
    # Recursively look in sets of figurate numbers for matches of cyclical form
    if len(sets) == 0:
        if match_cycle(num, match[0]):
            sum = num
            for a in range(0, len(match)):
                sum += match[a]
            print(f'Matches to {num} are {match}, sum is {sum}')
            return True
        else:
            return False
    else:
        if match is None:
            match = []
        new_sets = copy.deepcopy(sets)
        active_set = sets[0]
        new_sets.pop(0)
        for num2 in active_set:
            if (match_cycle(num, num2)):
                match.append(num)
                result = find_chains(num2, match, new_sets)
                match.pop()
                return result

tri = limit_numbers(1000, 10000, coef=[1,-1,2])
quad = limit_numbers(1000, 10000, coef=[1,0,1])
pent = limit_numbers(1000, 10000, coef=[3,1,2])
hexa = limit_numbers(1000, 10000, coef=[2,1,1])
hept = limit_numbers(1000, 10000, coef=[5,3,2])
octa = limit_numbers(1000, 10000, coef=[3,2,1])

number_sets = [hept,hexa,pent,quad,tri]
match_start = []
active_set = octa

set_iterations = list(itertools.permutations(number_sets))
for set_iteration in set_iterations:
    sets_to_test = list(set_iteration)
    for num in active_set:
        find_chains(num, match_start, sets_to_test)