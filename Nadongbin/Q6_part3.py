import numpy as np
from queue import PriorityQueue

def solution(food_times, k):
    que = PriorityQueue()
    
    # lower boundary check
    if sum(food_times) < k:
        return -1
    
    # add elements
    for i in range(len(food_times)):
        que.put((food_times[i], i+1))
        
    prev_food_time = 0
    
    for i in range(len(food_times)):
        food_time, food_num  = que.get()
        food_k = (que.qsize()+1)*(food_time-prev_food_time)
        if food_k <= k:     
            k -= food_k
            prev_food_time = food_time
            if que.empty():
                return -1  
        else:
            # consider corner case
            # get all indexes
            left_food_nums = [food_num]
            while not que.empty():
                left_food_nums += [que.get()[1]]
            
            left_food_nums = sorted(left_food_nums)
            
            final_idx = k % len(left_food_nums)
            final_food_num = int(left_food_nums[final_idx])
            return final_food_num
            
            
    answer = -1
    return answer
