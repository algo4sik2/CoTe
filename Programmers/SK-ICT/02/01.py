from itertools import combinations
from collections import defaultdict

def solution(goods):
    search_word = defaultdict(set)
    for good in goods:
        for i,j in combinations(range(len(good)+1),2):
            search_word[good].add(good[i:j])
    answer = []
    for good in goods:
        onlyit = search_word[good].copy()
        for i, j in search_word.items():
            if i!=good: onlyit -= j
        onlyit = sorted(onlyit, key=lambda x:len(x))
        onlyit = sorted([word for word in onlyit if len(word)==len(onlyit[0])])
        if onlyit: answer.append(' '.join(onlyit))
        else: answer.append('None')
    return answer