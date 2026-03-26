from collections import Counter

def solution(participant, completion):
    answer = ''
    counter_answer = Counter(participant)-Counter(completion)
    answer = list(counter_answer.keys())[0]
    return answer

