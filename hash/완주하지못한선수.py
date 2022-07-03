import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    print(type(answer.keys()))
    
    return list(answer.keys())[0]
