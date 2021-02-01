#!/usr/bin/python3
import math
import sys
import time


def checkIfPrime(a):
    for i in range(2, math.floor(a/2) + 1):
        if a % i == 0:
            return False
    return True


def printWhetherPrime(listOfNumbers):
    for number in listOfNumbers:
        print(number, ':', checkIfPrime(int(number)))


def printNonPrimes(listOfNumbers):
    print('Numbers that aren\'t prime:')
    for i in listOfNumbers:
        if not checkIfPrime(int(i)):
            print(i)


# listFactors seems to be the bottleneck. Slowest function by far.
def listFactors(a):
    factors = []
    # making this only check everything less than sqrt(a) made it orders of
    # magnitude faster
    for i in range(2, int((a ** 0.5) + 1)):
        if a % i == 0:
            factors.append(i)
    return factors


def listPrimeFactors(a):
    primeFactors = []
    factors = listFactors(a)
    for factor in factors:
        if checkIfPrime(factor):
            primeFactors.append(factor)
    return primeFactors


if __name__ == '__main__':
    numbers = sys.argv[1:]
    # numbers = [10, 684, 8461, 13195, 584378, 1268799, 84315679, 589743876,
    #            8976135794, 89761238010, 600851475143]
    numbers = [600851475143]
    for i in numbers:
        start = time.time()
        number = int(i)
        print('prime factors of', number, ':')
        print(listPrimeFactors(number))
        end = time.time()
        print('time to find prime factors:', end-start, 'seconds')
        print()

