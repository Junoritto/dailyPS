def solution(array, commands):
    answer = []
    for i,j,k in commands:
        candidates = sorted(array[i-1:j])
        answer.append(candidates[k-1])
    return answer