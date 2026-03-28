import math

def solution(progresses, speeds):
    answer = []
    mandays = []
    for i in range(len(progresses)):
        manday = math.ceil((100-progresses[i]) / speeds[i])
        mandays.append(manday)
        
    stack = []
    res = 1
    for m in mandays:
        if not stack or stack[-1] < m:
            stack.append(m)
            answer.append(res)
            res = 1
        else:
            res += 1
    
    answer.append(res)
    answer = answer[1:]
        
    return answer