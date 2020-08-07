# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.

num1, num2 = input(), input()

print(eval(f'{num1}+{num2}'))

# other solution

n1, n2 = 0, 0
d1, d2 = 10 ** (len(num1) - 1), 10 ** (len(num2) - 1)

for i1, i2 in zip(num1, num2):
    n1 += (ord(i1) - ord('0')) * d1
    d1 //= 10

    n2 += (ord(i2) - ord('0')) * d2
    d2 //= 10

print(n1 + n2)
