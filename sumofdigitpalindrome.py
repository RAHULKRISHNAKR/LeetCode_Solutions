'''Given a number n.Find if the digit sum(or sum of digits) of n is a Palindrome number or not.

Note: A Palindrome number is a number that stays the same when reversed. Example- 121 , 131 , 7 etc'''
def is_digit_sum_palindrome(n):
    """Checks if the sum of digits of a number is a palindrome.

    Args:
        n: The input number.

    Returns:
        True if the sum of digits is a palindrome, False otherwise.
    """

    if n < 0:
        return False

    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10

    # Efficient palindrome check
    return str(digit_sum) == str(digit_sum)[::-1]
