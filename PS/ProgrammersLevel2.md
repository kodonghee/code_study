#### 1. 멀쩡한 사각형

```python
import math  # math library 사용

def solution(w,h):
    
    # w와 h가 서로소일 때 사각형의 갯수를 구하는 방법
    if math.gcd(w, h) == 1:
        return w*h - (w + h - 1)  # 대각선이 지나갈 때마다 사각형이 가로, 세로의 길이만큼 나눠짐
    else:
        new_w = w // math.gcd(w, h)
        new_h = h // math.gcd(w, h)
        return w*h - ((new_w*new_h - solution(new_w, new_h))*math.gcd(w, h))
```





#### 2. 프린터

* 스택 / 큐

```python
def solution(priorities, location):
    from collections import deque
    qu = deque([(v, i) for i, v in enumerate(priorities)])
    count = 0
    
    while len(qu):
        
        doc = qu.popleft()
        
        
        # qu에 아무것도 남아 있지 않을 경우도 고려
        # 고려하지 않을 경우 max(qu)[0]를 구할 수 없는 경우 발생
        if qu and doc[0] < max(qu)[0]:
            qu.append(doc)
    
        else:
            count += 1
            if doc[1] == location:
                break
    
    return count
```





#### 3. 다리를 지나는 트럭

* 스택 / 큐

```python
def solution(bridge_length, weight, truck_weights):
    
    from collections import deque
    
    waiting = deque(truck_weights)
    moving = deque([])  # 다리를 지나고 있는 트럭의 queue
    # 다리를 지나면 moving queue에서 삭제해주기 위해 다리를 건너기 시작한 시점을 저장
    time = deque([])
    sec = 1
    
    while True:
        
        if time and sec - time[0] == bridge_length:
            moving.popleft()
            time.popleft()
        
        if waiting and sum(moving) + waiting[0] <= weight:
            moving.append(waiting.popleft())
            time.append(sec)
            
        if len(moving) == 0:
            break
            
        sec += 1
    
    return sec
```





#### 4. 스킬트리

```python
def solution(skill, skill_trees):

    count = 0 # 조건에 맞는 tree일 때마다 하나씩 세기

    for tree in skill_trees:

        rem = []
        for alp in tree:
            if alp in skill:
                rem.append(alp)

        if rem is None or rem == list(skill)[:len(rem)]:
            count += 1

    return count
```





#### 5. 기능개발

* 스택 / 큐

```python
# 기능을 개발하는 데 걸리는 일 수 계산
def day(prog, speed):
    rem = 100 - prog
    if rem % speed == 0:
        return rem // speed
    else:
        return rem // speed + 1
    
    
def solution(progresses, speeds):
    
    num_list = []
    count = 1
    max_day = day(progresses[0], speeds[0])
    
    for i in range(1, len(progresses)):
        
        if day(progresses[i], speeds[i]) <= max_day:
            count += 1
        # 마지막 기능이 아닌 경우 max_day보다 더 많은 시간이 걸리는 기능이 등장했을 때만
        # num_list에 count 추가 & max_day 변경
        else:
            num_list.append(count)
            max_day = day(progresses[i], speeds[i])
            count = 1
           
        # 마지막 기능이라면 num_list에 count를 반드시 추가
        if i == len(progresses)-1:
            num_list.append(count)
    
    
    return num_list
```





#### 6. 124 나라의 숫자

* 더 간결한 코드를 작성하는 법이 많은 문제

```python
import math


def solution(n):
    order = 0
    a = 1

    while True:

        order += math.pow(3, a)

        if order >= n:
            break

        a += 1
    fix = a
    number = ""


    while True:
		# 이 부분을 먼저 변수에 저장해 놓고 코드를 작성하지 않으면 런타임 오류
        start1 = order - pow(3, a)
        start2 = order - pow(3, a) + pow(3, a)//3
        start3 = order - pow(3, a) + 2 * pow(3, a)//3

        if n > start1 and n <= start2:
            number += "1"
            order = start2

        elif n > start2 and n <= start3:
            number += "2"
            order = start3
        else:
            number += "4"

        a -= 1

        if len(number) == fix:
            break

    return number
```

