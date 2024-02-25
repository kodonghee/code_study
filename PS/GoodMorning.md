#### 4형제 아침 안부 묻기

* `solution`

  * 4형제 아침 안부 묻기

  ```python
  def solution(N, house):
    answer = 0
    for i in range(len(house)):
        for j in range(len(house[0])):
            if house[i][j] == 1:
                locx1 = i
                locy1 = j
            elif house[i][j] == 2:
                locx2 = i
                locy2 = j
            elif house[i][j] == 3:
                locx3 = i
                locy3 = j
            elif house[i][j] == 4:
                locx4 = i
                locy4 = j
            else:
                continue
    
    answer += abs(locx1 - locx4) + abs(locy1 - locy4)
    answer += abs(locx2 - locx1) + abs(locy2 - locy1)
    answer += abs(locx3 - locx2) + abs(locy3 - locy2)
    answer += abs(locx4 - locx3) + abs(locy4 - locy3)
    
    return answer
  ```
