#### 수식 최대화

* 2020 카카오 인턴십

* `solution`

  * 해커톤 대회에 참가하는 모든 참가자들에게는 숫자들과 3가지의 연산문자(`+, -, *`) 만으로 이루어진 연산 수식이 전달되며, 참가자의 미션은 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출
  * 참가자에게 주어진 연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때, 우승 시 받을 수 있는 가장 큰 상금 금액을 return

  ```python
  def solution(expression):
      
      op = []
      for c in expression:
          if not c.isdigit():
            op.append(c)
      op = set(op)
      op = list(op)
  
      if len(op) == 0:
          return int(expression)
      elif len(op) == 1:
          return abs(eval(expression))
      elif len(op) == 2:
          m = 0
          for o in op:
              new = expression.split(o)
              s = ""
              for i in range(len(new)):
                  if i != len(new) - 1:
                      s += str(eval(new[i])) + o
                  else:
                      s += str(eval(new[i]))
              m = max(abs(eval(s)), m)
          return m
      else:
          m = 0
          op = [['*', '+', '-'], ['*', '-', '+'], ['-', '+', '*'], ['-', '*', '+'], ['+', '*', '-'], 
                ['+', '-', '*']]
          for o in op:
              new = expression.replace(o[1], o[1] + ' ')
              new = new.replace(o[2], o[2] + ' ')
              new = new.split()
              s = ""
              for i in range(len(new)):
                  if i != len(new) - 1:
                      s += str(eval(new[i][:-1])) + new[i][-1]
                  else:
                      s += str(eval(new[i]))
              new = s.split(o[2])
              s = ""
              for i in range(len(new)):
                  if i != len(new) - 1:
                      s += str(eval(new[i])) + o[2]
                  else:
                      s += str(eval(new[i]))
      
             m = max(abs(eval(s)), m)
  
          return m
  ```