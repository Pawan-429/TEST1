def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


# Example usage
print(is_palindrome("madam"))      # True
print(is_palindrome("hello"))      # False
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
