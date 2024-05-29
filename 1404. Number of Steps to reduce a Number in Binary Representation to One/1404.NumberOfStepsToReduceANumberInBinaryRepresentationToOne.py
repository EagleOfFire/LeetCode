def numSteps(s: str) -> int:
    num = int(s, 2)
    count = 0
    while num > 1:
        if (num % 2) == 0:
            num //= 2
        else:
            num += 1
        count += 1
    return count


#print(numSteps("1101"))
print(numSteps("1111011110000011100000110001011011110010111001010111110001"))
