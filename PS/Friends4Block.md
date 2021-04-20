#### 프렌즈4블록

* `solution`

  * "프렌즈4블록"
  * 같은 모양의 카카오프렌즈 블록이 2x2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임
  * 입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력

  ```python
  import numpy as np
  
  def solution(m, n, board):
      answer = 0
      if m <= 1:
          return answer
      
      arr = []
      for line in board:
          arr.append(list(line))
  
      while True:
          cnt = 0
          a = np.zeros((m, n))
          for i in range(m - 1):
              for j in range(n - 1):
                  if arr[i][j] != 1 and arr[i][j] == arr[i][j + 1]:
                      if arr[i + 1][j] == arr[i + 1][j + 1] and arr[i][j] == arr[i + 1][j]:
                          cnt += 1
                          a[i][j] = 1
                          a[i][j + 1] = 1
                          a[i + 1][j] = 1
                          a[i + 1][j + 1] = 1
          if cnt == 0:
              break
  
          for i in range(m):
              for j in range(n):
                  if a[i][j] == 1:
                      arr[i][j] = 1
  
          answer += int(a.sum())
          
          while True:
              cnt = 0
              for i in range(m - 1):
                  for j in range(n):
                      if arr[i][j] != 1 and arr[i + 1][j] == 1:
                          cnt += 1
                          arr[i + 1][j] = arr[i][j]
                          arr[i][j] = 1
              if cnt == 0:
                  break
  
      return answer
  ```