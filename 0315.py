## 거꾸로 읽어도 똑같은 문자 찾기

def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - (i + 1)]:
            return False
    return True
    

## 배열 내에서 특정 값 찾기 (선형 탐색)

def linear_search(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None
