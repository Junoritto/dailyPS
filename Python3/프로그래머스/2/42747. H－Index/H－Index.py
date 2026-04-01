def solution(citations):
    answer = 0
    citations.sort()
    l = len(citations)
    for i in range(l):
        if l-i <= citations[i]:
            return l-i
    return answer