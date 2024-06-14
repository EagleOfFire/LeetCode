def mySqrt(x: int) -> int:
    count = 0
    odd = 0
    while x >= 0:
        if odd % 2 != 0:
            x -= odd
            count += 1
        odd += 1
    return count-1


print(mySqrt(4))
print(mySqrt(8))
