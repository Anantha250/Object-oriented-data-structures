def backtrack(tasks, k, groups, memo):
    state = tuple(sorted(groups)) 
    if state in memo:  
        return memo[state]
    
    if not tasks: 
        return max(groups) 

    current_task = tasks.pop(0)  
    min_time = float('inf') 

    for i in range(k): 
        groups[i] += current_task
        min_time = min(min_time, backtrack(tasks[:], k, groups, memo)) 
        groups[i] -= current_task 
        
        if groups[i] == 0:  
            break

    tasks.insert(0, current_task) 
    memo[state] = min_time 
    return min_time

def min_time_to_finish_tasks(tasks, k):
    groups = [0] * k  
    memo = {}  
    return backtrack(tasks, k, groups, memo)

input_data = input("Enter jobs and number of workers : ").split("/")
tasks = list(map(int, input_data[0].split()))
k = int(input_data[1])



print(f"Minimum time to complete jobs with {k} workers is {min_time_to_finish_tasks(tasks, k)}")

