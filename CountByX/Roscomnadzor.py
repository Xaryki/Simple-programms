from string import punctuation

word = ""


def palindrome(word: str):
    if not word:
        return False
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] in punctuation:
            left += 1
            continue
        elif word[right] in punctuation:
            right -= 1
            continue
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def palindrome_2(word: str):
    left = ''
    right = ''
    return True
print(palindrome(word))