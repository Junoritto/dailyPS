from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    runtime = 0
    cnt = 0
    target_cnt = len(truck_weights)
    current_weight = 0
    while True:
        runtime += 1
        target = bridge.popleft()
        if target > 0:
            cnt += 1
            current_weight -= target
            if cnt == target_cnt:
                return runtime
        if truck_weights and (current_weight + truck_weights[0]) <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
            