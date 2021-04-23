#### 후보키

* 2019 KAKAO BLIND RECRUITMENT

* 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.

  * 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
  * 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

* `solution`

  * 릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의 개수를 return

  ```python
  def solution(relation):
      if len(relation) == 1:
          return len(relation[0])
  
      ck = []
      for i in range(len(relation[0])):
          ck.append(i)
  
      answer = 0
  
      for i in range(len(relation[0])):
          a = []
          for data in relation:
              if data[i] in a:
                  break
              a.append(data[i])
          if len(a) == len(relation):
              ck.remove(i)
              answer += 1
  
      from itertools import combinations
  
      c = 2
      rm = []
      while len(ck) >= c:
          arr = list(combinations(ck, c))
  
          for pair in arr:
              b = []
              for data in relation:
                  tar = []
                  for i in range(c):
                      tar.append(data[pair[i]])
                  if tar in b:
                      break
                  b.append(tar)
  
              if len(b) == len(relation):
                  cnt1 = 0
                  for n in rm:
                      cnt = 0
                      for m in n:
                          if m in pair:
                              cnt += 1
                      if cnt == len(n):
                          cnt1 += 1
                          break
                  if cnt1 == 0:
                      answer += 1
                      rm.append(pair)
  
          c += 1
  
      return answer
  ```