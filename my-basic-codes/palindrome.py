#palindrome is a word which is same as its reverse 
def palindrome(s):
    return s==s[::-1]
print(palindrome("Digvijay"))
print(palindrome("racecar"))
