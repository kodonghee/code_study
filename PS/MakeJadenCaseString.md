#### JadenCase 문자열 만들기

* `solution`

  * JadenCase: 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열
  * 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 return

  ```python
  def solution(s):
      answer = ''
      
      for i in range(len(s)):
          if (i == 0 or s[i - 1] == " ") and s[i].isalpha():
              answer += s[i].upper()
          elif s[i].isalpha():
              answer += s[i].lower()
          else:
              answer += s[i]
      
      return answer
  ```