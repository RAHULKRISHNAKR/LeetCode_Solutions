'''
A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
'''

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base_k(num: int, base: int) -> str:
            res = []
            while num > 0:
                res.append(str(num % base))
                num //= base
            return ''.join(res[::-1])

        def generate_palindromes():
            # Single digit palindromes
            for i in range(1, 10):
                yield i
            length = 1
            while True:
                # Even-length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])
                # Odd-length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    for mid in '0123456789':
                        yield int(s + mid + s[::-1])
                length += 1

        count = 0
        total = 0
        for num in generate_palindromes():
            if is_palindrome(to_base_k(num, k)):
                total += num
                count += 1
                if count == n:
                    break
        return total
