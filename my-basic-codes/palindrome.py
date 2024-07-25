#palindrome is a word which is same as its reverse 
def palindrome(s):
    return s==s[::-1]

user_input = input("Enter a string to check palindrome: ")
palindrome_string = palindrome(user_input)
print(("wether the input string is palindrome:", palindrome_string))
#print(palindrome("Digvijay"))
#print(palindrome("racecar"))

