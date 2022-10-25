def sumofDigits(n):
    assert int(n) == n or n >=0, "number has to be a positive integer"
    if len(str(n)) == 1:
        return n
    else:
        return int(n % 10) + sumofDigits(int(n/10))

result = sumofDigits(41)
print(result)