def findLargestPower(n):
    x = 0
    while ((1 << x) <= n):
        x += 1
    return x - 1


def countsetbits(n):
    if (n <= 1):
        return n
    x = findLargestPower(n)
    return (x * pow(2, (x - 1))) + (n - pow(2, x) + 1) + countsetbits(n - pow(2, x))


def solution(X, Y):
    countsetbits()


if __name__ == '__main__':
    print("********** Main *************")

    solution(1, 7)
    # solution(1007, 1010)
    # solution(0, 1111111111)
    print("The number of bits : ", countsetbits(0))
    print("The number of bits : ", countsetbits(1))
    print("The number of bits : ", countsetbits(2))
    print("The number of bits : ", countsetbits(3))
    print("The number of bits : ", countsetbits(4))
    print("The number of bits : ", countsetbits(5))

    print("jib")
    print("The number of bits : ", countsetbits(6))
    print("The number of bits : ", countsetbits(7))

    print("jib")
    print("The number of bits : ", countsetbits(1008))
    print("The number of bits : ", countsetbits(1009))
    print("The number of bits : ", countsetbits(1010))

    print("jib")
    print("The number of bits : ", countsetbits(1000000000))
    print("The number of bits : ", countsetbits(1000000010))
    print("The number of bits : ", countsetbits(1111111111))
