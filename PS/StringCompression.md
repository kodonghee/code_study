### 문자열 압축

* 2020 KAKAO BLIND RECRUITMENT

```python
def solution(s):
    minimum = len(s)

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        count = ""
        for j in range(len(s) // i - 1):
            if s[j*i:i + j*i] == s[i + j*i:2 * i + j*i]:
                count += "1"
            else:
                count += "0"

        count0 = count.split('0')
        count1 = count.split('1')

        a = 0
        b = 0
        # 이 부분을 고려하지 않아서 많이 고생함
        # 한 문자열이 10번 반복되면 4a와 같이 두 자리가 아닌 10a 세 자리가 됨
        for c1 in count0:
            if len(c1) > 0:
                if len(c1) > 0 and len(c1) < 9:
                    a += i + 1
                elif len(c1) >= 9 and len(c1) <99:
                    a += i + 2
                elif len(d1) >= 99 and len(c1) < 999:
                    a += i + 3
                else:
                    a += i + 4

        for k in range(len(count1)):
            if len(count1[k]) > 0:
                if k == 0 or k == len(count1)-1:
                    b += len(count1[k])
                else:
                    b += len(count1[k]) - 1

        if a == 0:
            num = len(s)
        else:
            num = b * i + a


        if len(s) % i != 0:
            num += len(s) % i

        if num < minimum:
            minimum = num

    return minimum
```