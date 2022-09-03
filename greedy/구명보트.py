from collections import deque


def solution(people, limit):

    answer = 0

    people_deque = deque(sorted(people))

    while people_deque:

        max_wei = people_deque.pop()

        if people_deque and (max_wei+people_deque[0]) <= limit:

            people_deque.popleft()

        answer+=1





    return answer
