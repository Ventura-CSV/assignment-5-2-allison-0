def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def primeNumbers(begin, end):
    plist = []
    for n in range(begin, end + 1):
        if isPrime(n):
            plist.append(n)

    return plist


def main():
    begin = 0
    end = 20
    rlst = primeNumbers(begin, end)
    print(rlst)

    begin = 10
    end = 50
    rlst = primeNumbers(begin, end)
    print(rlst)


if __name__ == '__main__':
    main()
