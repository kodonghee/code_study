#### n진수 게임

* 2018 KAKAO BLIND RECRUITMENT

* `solution`

  * 튜브가 말해야 하는 숫자 `t`개를 공백 없이 차례대로 나타낸 문자열. 단, `10`~`15`는 각각 대문자 `A`~`F`로 출력한다.

  ```python
  def convert(num):
      if num >= 10:
          return chr(num + 55)
      else:
          return str(num)
  
  
  def solution(n, t, m, p):
      answer = ""
      total = ""
      i = 0
  
      while len(total) < t * m:
  
          start = i
          new = ""
          while True:
  
              new += convert(start % n)
              start = start // n
  
              if start < n:
                  if start != 0:
                      new += convert(start)
                  break
  
          total += new[::-1]
          i += 1
  
      for j in range(len(total)):
          if (j + 1) % m == p or (m == p and (j + 1) % m == 0):
              answer += total[j]
          if len(answer) == t:
              break
  
      return answer
  ```