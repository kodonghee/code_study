#### 게임 맵 최단거리

* 찾아라 프로그래밍 마에스터

* `solution`

  * 게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 **최솟값**을 return
  * 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return
  * BFS (넓이 우선 탐색)
  
  ```python
  from collections import deque
  
  def solution(maps):
      
      path = [[1,0], [-1, 0], [0,1], [0,-1]]
      
      h = len(maps)
      w = len(maps[0])
      
      check = [[-1 for _ in range(w)] for _ in range(h)]
      
      q = deque()
      q.append([0,0])
      
      check[0][0] = 1
  
      while q:
          b, a = q.popleft()
  
          for i in range(4):
              next_b = b + path[i][0]
              next_a = a + path[i][1]
  
              if -1 < next_b < h and -1 < next_a < w:
                  if maps[next_b][next_a] == 1:
                      if check[next_b][next_a] == -1:
                          check[next_b][next_a] = check[b][a] + 1
                          q.append([next_b, next_a])
  
      answer = check[-1][-1]
      return answer
  ```