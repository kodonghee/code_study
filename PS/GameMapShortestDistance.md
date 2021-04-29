#### 게임 맵 최단거리

* 찾아라 프로그래밍 마에스터

* `solution`

  * 게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 **최솟값**을 return
  * 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return

  ```python
  def solution(maps):
      answer = 1
      loc = (0, 0)
      h = len(maps)
      w = len(maps[0])
  
      while True:
          a = loc[0]
          b = loc[1]
  
          if b == w - 1:
              if a + 1 < h and maps[a + 1][b] == 1:
                  loc = (a + 1, b)
                  answer += 1
              else:
                  return -1
          elif a == h - 1:
              if b + 1 < w and maps[a][b + 1] == 1:
                  loc = (a, b + 1)
                  answer += 1
              else:
                  return -1
          else:
  
              if b + 1 < w and maps[a][b + 1] == 1:
                  loc = (a, b + 1)
                  answer += 1
              elif a + 1 < h and maps[a + 1][b] == 1:
                  loc = (a + 1, b)
                  answer += 1
              elif a - 1 >= 0 and maps[a - 1][b] == 1:
                  loc = (a - 1, b)
                  answer += 1
              elif b - 1 >= 0 and maps[a][b - 1] == 1:
                  loc = (a, b - 1)
                  answer += 1
              else:
                  return -1
  
          if loc == (h - 1, w - 1):
              break
              
      return answer
  ```