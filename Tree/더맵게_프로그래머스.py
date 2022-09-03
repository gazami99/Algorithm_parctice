import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    tmp = 0
    
    while len(scoville) >1 and scoville[0] < K:
        
        tmp = heapq.heappop(scoville)
        heapq.heappushpop(scoville,scoville[0]*2+tmp)
        answer +=1
    
    if scoville[0] < K :
        
        answer = -1
    
    return answer
