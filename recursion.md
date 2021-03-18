## 재귀함수 (recursion)

* 자기 자신을 호출하는 함수

```python
def countdown(n):
    if n > 0:
        print(n)
        countdown(n -1)
```

> factorial

* 재귀적으로 문제를 푼다는 것 = **부분 문제**의 답을 이용해서 기존 문제를 푸는 것
  * n = 0 인 경우 n! = 1                         *(base case)*
  * n > 0 인 경우 n! = (n-1)! x n            *(recursive case)*

```python
def factorial(n):
    if n == 0
    	return 1
    return factorial(n-1) * n
```

