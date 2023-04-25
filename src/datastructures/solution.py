

def countsetbits(A):
    count = 0
    while (A != 0):
        A = A & (A - 1)
        count = count + 1
    return (count)


def solution(X, Y):
    fibs = {1, 2, 3, 5, 8, 13, 21, 34}

    ans = 0
    for i in range(X+1, Y+1):
        # print(i)
        setBits = countsetbits(i)
        print("setBits in ", i)
        print(setBits)
        if setBits in fibs:
            ans = ans + 1
    print("ans", ans)
    return ans

if __name__ == '__main__':
    print("********** Main *************")

    # solution(1, 7)
    # solution(1007, 1010)
    solution(0, 1111111111)
    # print("The number of bits : ", countsetbits(0))
    # print("The number of bits : ", countsetbits(1))
    # print("The number of bits : ", countsetbits(2))
    # print("The number of bits : ", countsetbits(3))
    # print("The number of bits : ", countsetbits(4))
    # print("The number of bits : ", countsetbits(5))
    #
    # print("jib")
    # print("The number of bits : ", countsetbits(6))
    # print("The number of bits : ", countsetbits(7))
    #
    # print("jib")
    # print("The number of bits : ", countsetbits(1008))
    # print("The number of bits : ", countsetbits(1009))
    # print("The number of bits : ", countsetbits(1010))
    #
    # print("jib")
    # print("The number of bits : ", countsetbits(1000000000))
    # print("The number of bits : ", countsetbits(1000000010))
    # print("The number of bits : ", countsetbits(1111111111))
