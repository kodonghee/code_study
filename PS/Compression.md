#### 압축

* 2018 KAKAO BLIND RECRUITMENT

* LZW (Lempel-Ziv-Welch) 압축

* `solution`

  * 입력으로 영문 대문자로만 이뤄진 문자열 `msg`가 주어지면 이를 압축한 후의 사전 색인 번호를 배열로 출력

  ```python
  def solution(msg):
      answer = []
  
      dic = {}
      for i in range(26):
          dic[chr(ord('A') + i)] = i + 1
  
      i = 0
      c = 0
      while i <= len(msg) - 1:
          if i == len(msg) - 1:
              answer.append(dic[msg[i]])
              break
          for j in range(i + 1, len(msg)):
              if j == len(msg) - 1 and msg[i:j + 1] in dic.keys():
                  answer.append(dic[msg[i:j + 1]])
                  index = j + 2
                  break
              if msg[i:j + 1] not in dic.keys():
                  answer.append(dic[msg[i:j]])
                  index = j + 1
                  break
  
          dic[msg[i:index]] = 27 + c
          i = index - 1
          c += 1
  
      return answer
  ```