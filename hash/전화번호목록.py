def solution(phone_book):
    answer = True

    hash_map = {}

    for i in sorted(phone_book):

        tmp_s = ''

        for j in i:

            tmp_s = tmp_s + j

            if tmp_s in hash_map:

                return False

        hash_map[i] = 0



    return answer
