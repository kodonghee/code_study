## Dynamic Programming

1. 최적 부분 구조 - 부분 문제들의 최적 답을 이용해 기존 문제의 최적의 답을 구할 수 있다는 ㅓㅅ
2. 중복되는 부분 문제 

### 1. Memoization

- 중복되는 계산은 한 번만 계산 후 메모

```python
def fib_memo(n, cache):
    cache = []
    for i in range(n):
        if i == 0 or i == 1:
            cache.append(1)
        else:
            cache.append(cache[i-2] + cache[i-1])
    
    return cache[-1]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)
```

> 새콤달콤 장사

* 가능한 최대 수익을 리턴시켜 주는 함수 `max_profit_memo`

```python
def max_profit_memo(price_list, count, cache):
    # price_list: 개수별 가격이 정리되어 있는 리스트
    # count: 판매할 새콤달콤 개수
    # cache: 개수별 최대 수익이 저장되어 있는 사전
    if count == 0:
        cache[0] = price_list[0]
        return cache[0]
    if count == 1:
        cache[1] = price_list[1]
        return cache[1]
    max = 0
    for i in range(1, count):
        if max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache) > max:
            max = max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache)
    
    if len(price_list) > count and price_list[count] > max:
        return price_list[count]
    cache[count] = max
    return cache[count]

    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)
```



### 2. Tabulation

* 처음부터 모두 계산 (상향식 접근)

```python
def fib_tab(n):
    tab = []
    for i in range(n):
        if i == 0 or i == 1:
            tab.append(1)
        else:
            tab.append(tab[i-2] + tab[i-1])
    return tab[n-1]
```