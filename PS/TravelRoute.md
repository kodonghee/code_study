#### 여행경로

* `solution`

  * 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return
  * 주어진 항공권을 모두 이용하여 여행경로를 짜려고 한다.
  * 항상 "ICN" 공항에서 출발

  ```python
  def solution(tickets):
      answer = ["ICN"]
      point = "ICN"
      plus = []
      
      for i in range(len(tickets)):
          nex = "ZZZ"
          cnt = 0
          for city in tickets:
              if city[0] == point and city[1] < nex:
                  if  i < len(tickets) - 1:
                      x = city[1]
                      for other in tickets:
                          if other[0] == city[1]:
                              cnt += 1
                              nex = city[1]
                  else:
                      nex = city[1]
                      cnt += 1
                      
          if cnt == 0:
              nex = x
              
          for i in range(len(tickets)):
              if tickets[i] == [point, nex]:
                  tickets[i][0] = 0
                  break
                  
          if cnt == 0:
              plus.append(nex)
              plus.append(point)
              a = answer.pop()
              point = answer[-1]
              for i in range(len(tickets)):
                  if tickets[i] == [point, a]:
                      tickets[i][0] = 0
                      break
          else:
              point = nex
              answer.append(nex)
              
      if len(plus) == 0:
          return answer
      else:
          while len(plus) > 0 :
              answer.append(plus.pop())
          return answer
  ```

  