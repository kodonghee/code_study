## BruteForceAttack

* 무차별 대입 공격 
* 비효율적
* 가장 순진한 알고리즘 접근법
* 장점 : 직관적, 명확 / 답을 확실하게 찾을 수 있음

### 가장 가까운 두 좌표 찾기

* My answer
  * for문을 두 번 쓰지 않는 방법을 찾아보자.


```python
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


def closest_pair(coordinates):
    dis = []
    for i in range(len(coordinates) - 1):
        for j in range(len(coordinates) - i - 1):
            dis.append(distance(coordinates[i], coordinates[i + j + 1]))
    minimum = min(dis)

    for i in range(len(coordinates) - 1):
        for j in range(len(coordinates) - i - 1):
            if minimum == distance(coordinates[i], coordinates[i + j + 1]):
                return [coordinates[i], coordinates[i + j + 1]]
```

- 수정 후
  - 좌표 쌍을 계속 업데이트 해주는 방식을 이용하면 더 효율적인 코드가 완성된다.

```python
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


def closest_pair(coordinates):
    pair = [coordinates[0], coordinates[1]]
    
    for i in range(len(coordinates) -1):
        for j in range(i+1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]
    return pair        
```