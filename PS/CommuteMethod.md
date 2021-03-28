#### 출근하는 방법

* `staircase`

  * 총 계단 수 stairs와 한 번에 올라갈 수 있는 계단 수 possible_steps를 받아서 

    올라갈 수 있는 방법의 수를 효율적으로 찾아서 리턴하는 함수

  * stairs가 3, possible_steps가 [1, 2, 3]이면 계단 총 3칸을 1, 2, 3칸씩 갈 수 있을 때 오르는 방법의 수

```python
def staircase(stairs, possible_steps):
    if stairs == 0 or stairs == 1:
        return 1
    if stairs < 0:
        return 0
    alist = [1, 1]
    
    # Dynamic Programming - Tabulation
    # alist에 계단 수에 따른 올라가는 방법 수를 저장
    for i in range(2, stairs + 1):
        count = 0
        for step in possible_steps:
            count += staircase(i - step, possible_steps)
        alist.append(count)
        
    return alist[stairs]
```