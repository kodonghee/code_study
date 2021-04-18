#### 방금그곡

* 2018 KAKAO BLIND RECRUITMENT

* [3차] 방금그곡

* `solution`

  * 입력으로 네오가 기억한 멜로디를 담은 문자열 `m`과 방송된 곡의 정보를 담고 있는 배열 `musicinfos`가 주어진다.
  * 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다.
  * 네오가 찾으려는 음악의 제목을 return

  ```python
  def solution(m, musicinfos):
      
      melodies = []
      for music in musicinfos:
          arr = music.split(',')
          start = arr[0].split(':')
          end = arr[1].split(':')
          
          if start[0] != "00" and end[0] == "00":
              end[0] = "24"
          
          if start[1] <= end[1]:
              t = 60 * (int(end[0]) - int(start[0])) + int(end[1]) - int(start[1])
          else:
              t = 60 * (int(end[0]) - int(start[0]) - 1) + 60 + int(end[1]) - int(start[1])
          
          cnt = 0
          for n in arr[3]:
              if n.isalpha():
                  cnt += 1
                  
          r = t % cnt
          cnt2 = 0
          mel = ""
          for n in arr[3]:
              if n.isalpha():
                  mel += n
                  cnt2 += 1
              else:
                  mel += n
              if cnt2 > r:
                  mel = mel[:-1]
                  break
  
          melody = (t // cnt) * arr[3] + mel
          
          if m in melody:
              if melody.count(m) == 1:
                  if melody.find(m) + len(m) == len(melody): 
                      melodies.append([t, arr[2]])
                  elif melody[melody.find(m) + len(m)] != "#":
                      melodies.append([t, arr[2]])
              else:
                  while m in melody:
                      a = melody.find(m) + len(m)
                      if a == len(melody) or melody[a] != "#":
                          melodies.append([t, arr[2]])
                          break
                      else:
                          melody = melody[a + 1:]
                  
      
      if len(melodies) == 0:
          return "(None)"
      elif len(melodies) == 1:
          return melodies[0][1]
      else:
          max_t = 0
          for melody in melodies:
              if melody[0] > max_t:
                  max_t = melody[0]
          for melody in melodies:
              if melody[0] == max_t:
                  return melody[1]
  ```