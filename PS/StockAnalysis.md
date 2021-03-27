#### 주식 분석 문제

* `max_profit`
  * 일별 주식 가격이 들어 있는 stock_list를 받고 최대 수익을 리턴하는 함수 

```python
def max_profit(stock_list):
    max1 = stock_list[1] - stock_list[0]
    for i in range(len(stock_list) - 1):
        if max(stock_list[i+1:]) - stock_list[i] > max1:
            max1 = max(stock_list [i+1:]) - stock_list[i]
    return max1
```