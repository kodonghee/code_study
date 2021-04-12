#### 입국심사

* `solution`

  * 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return

  ```python
  def solution(n, times):
      times.sort()
      answer = 0
      t = []
      for i in range(len(times)):
          t.append(0)
      
      while n > 0:
          for i in range(len(t)):
              if t[i] == 0:
                  cnt = 0
                  for j in range(i):
                      if t[j] + times[j] < times[i]:
                          cnt += 1
                  if cnt == 0:
                      t[i] = times[i]
                      n -= 1
              if n == 0:
                  break
          
          
          a = t.remove(0)
          m = min(for time > 0 in t)
                  
          if n == 0:
              answer += max(t)
          else:
              answer += m
              
          for i in range(len(t)):
              if t[i] != 0:
                  t[i] = t[i] - m
  
      return answer
  ```