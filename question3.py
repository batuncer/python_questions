# Please create a function to check whether a word is a palindrome. If it is a palindrome, return
# the word, otherwise return the reverse of the word. Please convert the word to lower case and
# return .
# Sample Input 1: Python
# Sample Output 1: nohtyp
# Sample Input 2: eYE
# Sample Input 2: eye

def lowerCase_palindrome(word):
    if word.islower():
        return word[::-1]     # if word is lowercase return palindrome word
    else:
        return word[::-1].lower()  

word1 = "Python"
word2 = "eYE"

print(lowerCase_palindrome(word1))  # Output: nohtyP
print(lowerCase_palindrome(word2))  # Output: eye
