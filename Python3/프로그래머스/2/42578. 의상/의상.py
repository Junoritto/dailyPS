from collections import Counter

def solution(clothes):
    answer = 1
    clothes_dic = Counter([c[1] for c in clothes])
    for k, v in clothes_dic.items():
        answer *= v+1
    answer -= 1
    return answer