def correct(p):

    check = bal = 0
    u = ""
    v = ""

    if p == "":

        return p

    for j,i in enumerate(p):

        if i == '(':
            bal += 1
        else:
            bal += -1

        if bal < 0:

            check = 1
        if not j==0 and bal ==0:
            u = p[:j+1]
            v = p[j+1:]
            break

    if check:

        u = u[1:-1]

        u = u.replace('(','0')
        u = u.replace(')','(')
        u = u.replace('0',')')


        return  '('+correct(v)+ ')' +u
    else:  

        return u + correct(v)


def solution(p):

    answer = correct(p)

    return answer
