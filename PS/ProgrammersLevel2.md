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