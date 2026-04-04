def solution(answers):
    answer = []
    max_num = 10000
    one = [1,2,3,4,5]
    one = one * (max_num // len(one) + 1)
    two = [2,1,2,3,2,4,2,5]
    two = two * (max_num // len(two) + 1)
    three = [3,3,1,1,2,2,4,4,5,5]
    three = three * (max_num // len(three) + 1)
    
    scoreboard = {1:0,2:0,3:0}
    for i in range(len(answers)):
        if one[i] == answers[i]:
            scoreboard[1] += 1
        if two[i] == answers[i]:
            scoreboard[2] += 1
        if three[i] == answers[i]:
            scoreboard[3] += 1
    
    max_score = max(scoreboard.values())
    for k,v in scoreboard.items():
        if v == max_score:
            answer.append(k)
    return answer