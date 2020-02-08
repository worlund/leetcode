def addStrings(num1: str, num2: str) -> str:
    i = len(num1) - 1
    j = len(num2) - 1

    res = ""
    carry = 0
    while i >= 0 or j >= 0:
        n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
        partial_sum = n1 + n2 + carry
        carry = partial_sum//10
        res += str(partial_sum%10)

        i -= 1
        j -= 1
    res = res+str(carry) if carry > 0 else res
    return res[::-1]

n, m = "9999999999", "1"
r = addStrings(n, m)
print(r, int(n)+int(m))