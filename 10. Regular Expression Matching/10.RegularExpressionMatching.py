def isMatch(s: str, p: str) -> bool:
    if len(s) == 0 or (s == p):
        return True
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    return False


print(isMatch("aa", "a"))
# print(isMatch("aa", "a*"))
# print(isMatch("ab", ".*"))
# print(isMatch("aab", "c*a*b"))
