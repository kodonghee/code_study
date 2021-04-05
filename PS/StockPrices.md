#### 주식가격

* `solution`

  * 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하는 함수
  * 입출력 예
    * prices = [1, 2, 3, 2, 3]
    * return = [4, 3, 1, 1, 0]

  ```python
  def solution(prices):
      answer = []
      for i in range(len(prices) - 1):
          cnt = 0
          for j in range (i + 1, len(prices)):
              if prices[j] < prices[i]:
                  answer.append(j - i)
                  cnt += 1
                  break
          if cnt == 0 :
              answer.append(len(prices) - 1 - i)
              
      answer.append(0)
              
      return answer
  ```