#### 괄호 변환 문제

* Programmers Level 2

* ``solution``

  * "균형잡힌 괄호 문자열" : '('의 개수 = ')'의 개수
  * "올바른 괄호 문자열" : "균형잡힌 괄호 문자열" && '('와 ')'의 괄호의 짝도 모두 맞을 경우
  * "균형잡힌 괄호 문자열"p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return

  ```java
  public static String arr_to_s(String [] arr){
          String s = "";
          for(int i=0;i < arr.length; i++){
              s += (String)arr[i];
          }
          return s;
      }
      public static String solution(String p){
          String [] arr = new String[p.length()];
          arr = p.split("");
  
  //        String answer = "";
  
          if (p == ""){
              return p;
          }
  
          if (arr[0] == ")"){
              String []arr_mid = new String[arr.length -2];
              for (int i = 1; i < arr.length - 1; i++){
                  arr_mid[i - 1] = arr[i];
              }
              return "(" + solution(arr_to_s(arr_mid))+")";
          }
          int a = 0;
          int b = 0;
          for (int i = 0;i < p.length();i++){
              if (arr[i] =="("){
                  a += 1;
              }else{
                  b += 1;
              }
              if (b > a){
                  String []arr1 = new String[i];
                  String []arr2 = new String[arr.length - i];
                  for (int j = 0; j < i; j++){
                      arr1[j] = arr[j];
                  }
                  for (int j = 0; j < arr.length - i; j++){
                      arr2[j] = arr[j+i];
                  }
                  return solution(arr_to_s(arr1)) + solution(arr_to_s(arr2));
              }
          }
          return p;
      }
  ```