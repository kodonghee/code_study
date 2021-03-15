## 거꾸로 읽어도 똑같은 문자 찾기

def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - (i + 1)]:
            return False
    return True
    
