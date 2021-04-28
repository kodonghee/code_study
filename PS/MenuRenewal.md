#### 메뉴 리뉴얼

* 2021 KAKAO BLIND RECRUITMENT

* `solution`

  * 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
  * 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
  * 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, "스카피"가 `추가하고 싶어하는` 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return

  ```python
  def solution(orders, course):
      answer = []
  
      from itertools import combinations
  
      for num in course:
          a = []
  
          comb = []
          for order in orders:
              if len(order) >= num:
                  comb += list(combinations(order, num))
  
          comb = set(comb)
          m = 2
  
          for com in comb:
              n_orders = orders.copy()
  
              cnt = 0
              for i in range(len(n_orders)):
                  if len(n_orders[i]) < num:
                      n_orders[i] = 0
                      cnt += 1
  
              for i in range(num):
                  for j in range(len(n_orders)):
                      if n_orders[j] != 0 and com[i] not in n_orders[j]:
                          cnt += 1
                          n_orders[j] = 0
                      if cnt == len(n_orders):
                          break
  
              if len(n_orders) - n_orders.count(0) > m:
                  a = []
                  m = len(n_orders) - n_orders.count(0)
                  n = list(com)
                  n.sort()
                  new = ""
                  for i in range(num):
                      new += n[i]
                  a.append(new)
              elif len(n_orders) - n_orders.count(0) == m:
                  n = list(com)
                  n.sort()
                  new = ""
                  for i in range(num):
                      new += n[i]
                  a.append(new)
  
          answer += a
  
      answer = set(answer)
      answer = list(answer)
      answer.sort()
  
  
      return answer
  ```