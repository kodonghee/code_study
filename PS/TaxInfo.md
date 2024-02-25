#### 세금 납부 정보 수집

* `solution`

  * 세금 납부 정보 수집

  ```python
  import numpy as np

  def solution(N, K, arr, queries):
    answer = [0 for _ in range(K)]
    arr = np.array(arr)
    num = 0
    
    for i in range(K):
        X, Y = queries[i][0], queries[i][1]
        if X == Y:
            num = len(np.where(arr == X)[0])
        else:
            num = len(np.where((arr >= X) & (arr <= Y))[0])
        answer[i] = num
        
    return answer
  ```
