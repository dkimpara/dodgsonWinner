#algorithm for heuristic GreedyScore
from math import floor

def greedy_score(C: list, c: int, V: list) -> tuple:
    """C is list of candidates 0 to m-1 (m candidates)
    V is matrix of votes, v[i][0] is least preferred, v[m] most preferred
    c is the candidate in question, int"""
    C_minus_c = [d for d in C if d != c] #candidates without c
    
    deficit, swaps = {}, {}
    for d in C_minus_c: #initialize counter variables
        deficit[d] = 0
        swaps[d] = 0
    
    for v in V:
        i = 0
        while v[i] != c:
            d = v[i]
            deficit[d] = deficit[d] - 1
            i += 1
        if i < len(v) - 1:
            d = v[i+1]
            swaps[d] = swaps[d] + 1
        i += 1
        while i <= len(v) - 1:
            d = v[i]
            deficit[d] = deficit[d] + 1
            i += 1

    confident = True
    #now calculate the score
    score = 0
    for d in C_minus_c:
        if deficit[d] >= 0:
            score += floor(deficit[d]/2) + 1
            if deficit[d] >= 2 * swaps[d]:
                confident = False
                score += 1

    return (score, confident)

def greedy_winner(C: list, c: int, V: list) -> tuple:
    winner = True
    cscore, confident = greedy_score(C,c,V)
    for d in C:
        if d != c: #only check with d that isn't c
            dscore, dcon = greedy_score(C,d,V)
            if dscore < cscore:
                winner = False
            if dcon == False:
                confident = False
    return (winner, confident)



