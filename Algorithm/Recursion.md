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

> 하노이의 탑

```python
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    peg = [1, 2, 3]
    peg.remove(start_peg)
    peg.remove(end_peg)
    rem = peg[0]
    
    if num_disks == 1:
        move_disk(num_disks, start_peg, end_peg)
    else:
        hanoi(num_disks -1, start_peg, rem)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks -1, rem, end_peg)
        
# num_disks = 원판 수, start_peg = 게임을 시작하는 기둥 번호, end_peg = 목표로 하는 기둥 번호 
```

