def solution(N, stages):
    data = []
    reached_cnt = len(stages)
    # initialize
    for i in range(1, N+1):
        curr_fail_cnt = stages.count(i)
        
        data += [[i, curr_fail_cnt/(reached_cnt+1e-9)]] # stage, fail rate
        reached_cnt -= curr_fail_cnt

    data.sort(key= lambda x: (-x[1], x[0]))
    
    answer = [x[0] for x in data]
    
    return answer
