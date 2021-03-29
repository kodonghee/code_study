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


## 배열 내에서 특정 값 찾기 (이진 탐색)

def binary_search(element, some_list):
    ori_list = some_list
    index = (len(some_list) -1) //2
    while len(some_list) > 0:
        if some_list[index] == element:
            for i in range(len(ori_list)):
                if ori_list[i] == element:
                    return i
        
        elif some_list[index] < element:
            some_list = some_list[index + 1:len(some_list)]
            index = (len(some_list) -1) //2
        else:
            some_list = some_list[0:index]
            index = (len(some_list) -1) //2
    return None
