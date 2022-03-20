from itertools import permutations

def solve(N,M):
    dp = permutations("123456789",N)

    c = 0
    for i in dp:
        temp =""
        for subb in i:
            temp += (str(subb)*2)
        if int(temp)%M == 0:
            c += 1
    return c


    


print(solve(1,7))