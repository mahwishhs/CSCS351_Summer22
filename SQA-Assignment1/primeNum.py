
def isPrimeNum(num):
    for i in range(2, num+1):
        if (num % i == 0) and num != i:
            isPrime = False
            break
        else:
            isPrime = True
        i += 1

    if isPrime:
        #print(num, "is Prime Number:")
        return True
    else:
        #print(num, "is Prime Number:")
        return False

