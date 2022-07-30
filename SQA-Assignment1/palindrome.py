def IsPalindrome(word):

    if len(word) == 0 or len(word) == 1:
        return True

    if word[0] == word[-1]:
        return IsPalindrome(word[1:-1])
    else:
        return False

#print(palindrome("maham"))







