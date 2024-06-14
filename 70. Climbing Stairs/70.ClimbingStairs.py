def climbStairs(self, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1

    # Initialize base cases
    prev2 = 1  # f(0)
    prev1 = 1  # f(1)

    # Compute the number of ways for each step from 2 to n
    for i in range(2, n + 1):
        current = prev1 + prev2
        # Update for the next iteration
        prev2 = prev1
        prev1 = current

    return prev1

