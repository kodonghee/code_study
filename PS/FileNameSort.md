#### 파일명 정렬

* 2018 KAKAO BLIND RECRUITMENT

* 파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.

  - HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
  - NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. `0`부터 `99999` 사이의 숫자로, `00000`이나 `0101` 등도 가능하다.
  - TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.

* 파일명을 세 부분으로 나눈 후, 다음 기준에 따라 파일명을 정렬한다.

  - 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다. 이때, 문자열 비교 시 대소문자 구분을 하지 않는다. `MUZI`와 `muzi`, `MuZi`는 정렬 시에 같은 순서로 취급된다.
  - 파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다. 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다. 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.
  - 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. `MUZI01.zip`과 `muzi1.png`가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.

* `solution`

  * 파일명 정렬 프로그램 구현

  ```python
  def solution(files):
      answer = []
  
      r = 0
      for file in files:
          for i in range(len(file)):
              if file[i].isdigit():
                  index = i
                  break
          for i in range(index, len(file)):
              if not file[i].isdigit():
                  answer.append((file[:index].lower(), int(file[index:i]), r))
                  break
              if i == len(file) - 1:
                  answer.append((file[:index].lower(), int(file[index:]), r))
          r += 1
  
      answer.sort(key=lambda x : x[0])
  
      c = 0
      for i in range(len(answer)):
          if i == len(answer) - 1 or answer[i][0] != answer[i+1][0]:
              b = answer[c:i+1]
              b.sort(key=lambda x : x[1])
              answer[c:i+1] = b
              c = i+1
  
      for i in range(len(answer)):
          a = files[answer[i][2]]
          answer[i] = a
  
      return answer
  ```