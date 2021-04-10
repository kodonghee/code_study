#### 오픈채팅방

* 2019 KAKAO BLIND RECRUITMENT

* `solution`

  * 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return

  ```python
  def last_name(record, user_id):
      for rec in record[::-1]:
          arr = rec.split()
          if arr[0] != "Leave" and arr[1] == user_id:
              return arr[2]
          
  
  def solution(record):
      answer = []
      d = {}
  
      for rec in record:
          arr = rec.split()
          if arr[0] == "Enter":
              if arr[1] not in d.keys():
                  d[arr[1]] = last_name(record, arr[1])
              answer.append(d.get(arr[1]) + "님이 들어왔습니다.")
          elif arr[0] == "Leave":
              answer.append(d.get(arr[1]) +"님이 나갔습니다.")
  
      return answer
  ```