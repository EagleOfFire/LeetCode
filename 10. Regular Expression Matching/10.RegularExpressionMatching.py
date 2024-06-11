def isMatch(s: str, p: str) -> bool:
    ans = False
    if "*" not in p and "." not in p and s != p:
        return False
    if ("*" not in p and "." not in p and s == p) or ".*" in p:
        return True
    for i in range(len(p)):
        if p[i] == "*":
            if s[i] == p[i-1]:
                ans = True
            else:
                ans = False
        if p[i] == ".":
            if s[i] != "":
                ans = True
            else:
                ans = False
        if p[i] == s[i]:
            ans = True
        else:
            ans = False
    return ans


print(isMatch("aa", "a"))
print(isMatch("aa", "a*"))
print(isMatch("ab", ".*"))
print(isMatch("aab", "c*a*b"))
