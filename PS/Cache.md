#### 캐시

* 2018 KAKAO BLIND RECRUITMENT

* `solution`

  * DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램
  * 캐시 교체 알고리즘 `LRU`(Least Recently Used) 사용
  * `cache hit`일 경우 실행시간은 `1`
  * `cache miss`일 경우 실행시간은 `5`

  ```python
  def solution(cacheSize, cities):
      answer = 0
      
      from collections import deque
      queue = deque([])
      
      for i in range(len(cities)):
          cities[i] = cities[i].lower()
      
      if cacheSize == 0:
          return 5 * len(cities)
      
      for city in cities:
          if len(queue) < cacheSize and city not in queue:
              queue.append(city)
              answer += 5
          elif len(queue) == cacheSize and city not in queue:
              queue.popleft()
              queue.append(city)
              answer += 5
          else:
              queue.remove(city)
              queue.append(city)
              answer += 1
      
      return answer
  ```