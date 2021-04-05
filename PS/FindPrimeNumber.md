#### 소수 찾기

* `solution`

  * 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return
  * permutations 안 쓰고 푸는 방법 연구 필요

  ```python
  from itertools import permutations
  
  def num_od(number): 
      if number == 0 or number == 1:
          return False
      if number == 2:
          return True
      for i in range(2, int(number)):
          if int(number) % i == 0:
              return False
              break
      return True
  
  def solution(numbers):
      answer = 0
      rem = []
      
      for i in range(1, len(numbers) + 1):
          nums = list(permutations(numbers, i))
          nums = set(nums)
          for num in nums:
              a = ""
              for j in range(i):
                  a += num[j]
              if num_od(int(a)) and int(a) not in rem:
                  rem.append(int(a))
                  answer += 1    
      
      return answer
  ```