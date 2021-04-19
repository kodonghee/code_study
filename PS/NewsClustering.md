#### 뉴스 클러스터링

* `solution`

  * `str1`과 `str2`의 두 문자열을 입력받고, 입력으로 들어온 두 문자열의 자카드 유사도 출력
  * 유사도 값은 0에서 1사이의 실수이므로, 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력

  ```python
  def solution(str1, str2):
      arr1 = []
      arr2 = []
  
      for i in range(len(str1) - 1):
          c = str1[i] + str1[i + 1]
          if c.isalpha():
              arr1.append(c.lower())
  
      for i in range(len(str2) - 1):
          c = str2[i] + str2[i + 1]
          if c.isalpha():
              arr2.append(c.lower())
  
      total = set(arr1 + arr2)
      andset = 0
      pluset = 0
  
      for s in total:
          a = arr1.count(s)
          b = arr2.count(s)
          andset += min(a, b)
          pluset += max(a, b)
      
      if pluset == 0:
          return 1 * 65536
  
      answer = int(float(andset / pluset) * 65536)
  
      return answer
  ```