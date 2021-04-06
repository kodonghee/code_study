#### 단속카메라

* `solution`

  * 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return
  * Try 1: 각 지점을 지나는 차량의 수를 세고 최댓값에 해당하는 지점에 카메라를 설치 / 그 지점을 지나는 차량은 배열에서 지우고 solution 함수 다시 불러오기
    * 각 지점을 도는 for문 + route를 도는 for문 ... 시간 초과 현상 발생

  ```python
  def remove_values_from_list(the_list, val):
      while val in the_list:
          the_list.remove(val)
  
  def solution(routes):
      answer = 0
      if len(routes) == 1:
          return 1
      if len(routes) == 0:
          return 0
  
      min = routes[0][0]
      max = routes[0][1]
      for i in range(len(routes)):
          if routes[i][0] < min:
              min = routes[i][0]
  
      for i in range(len(routes)):
          if routes[i][1] > max:
              max = routes[i][1]
  
      m_num = 0
  
      for point in range(min, max + 1):
          num = 0
          for route in routes:
              if point >= route[0] and point <= route[1]:
                  num += 1
          if num > m_num:
              m_num = num
              p = point
      print(p)
      for i in range(len(routes)):
          if p <= routes[i][1] and p >= routes[i][0]:
              routes[i] = 0
              print(routes)
  
      remove_values_from_list(routes, 0)
      new = routes
  
      return 1 + solution(new)
  ```

  * Try 2:  차량이 지나는 끝 지점 순서대로 배열을 정렬 / 첫 요소의 마지막 지점에 카메라 설치 (point) / 다음 요소의 첫 지점이 point보다 이전이라면 넘어가고 아니면 그 요소의 마지막 지점에 카메라 설치 ... 반복 
    * 코드도 짧고 시간도 매우 짧음
    * 자주 나오는 유형 

  ```python
  def solution(routes):
      answer = 1
      if len(routes) == 1:
          return 1
      routes.sort(key=lambda x:x[1])
      
      point = routes[0][1]
      for route in routes:
          if route[0] > point:
              point = route[1]
              answer += 1
  
      return answer
  ```