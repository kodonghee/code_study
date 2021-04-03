#### 괄호 변환 문제

* Programmers Level 2

* ``solution``

  * "균형잡힌 괄호 문자열" : '('의 개수 = ')'의 개수
  * "올바른 괄호 문자열" : "균형잡힌 괄호 문자열" && '('와 ')'의 괄호의 짝도 모두 맞을 경우
  * "균형잡힌 괄호 문자열"p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return

* Array로 풀이한 경우

  * 시간이 적게 걸림 

  ```java
  class Solution {
       public String arr_to_s(String [] arr){
          String s = "";
          for(int i=0;i < arr.length; i++){
              s += (String)arr[i];
          }
          return s;
      }
      
      public String solution(String p) {
          String [] arr = new String[p.length()];
          arr = p.split("");
  
          if (p == ""){
              return p;
          }
      
          int a = 0;
          int b = 0;
          for (int i = 0;i < arr.length;i++){
              if (arr[i].equals("(")){
                  a += 1;
              }else{
                  b += 1; }
  
              if (b == a && arr[0].equals("(")){
                  String []arr1 = new String[i + 1];
                  String []arr2 = new String[arr.length - i-1];
                  for (int j = 0; j < i+1; j++){
                      arr1[j] = arr[j];
                  }
                  for (int j = 0; j < arr.length - i -1; j++){
                      arr2[j] = arr[j+i+ 1];
                  }
                  return arr_to_s(arr1) + solution(arr_to_s(arr2));
              }
              if (a == b && arr[0].equals(")")){
                  String []arr1 = new String[i+1];
                  String []arr2 = new String[arr.length - i-1];
                  for (int j = 0; j < i+1; j++){
                      arr1[j] = arr[j];
                  }
                  for (int j = 0; j < arr.length - i-1; j++){
                      arr2[j] = arr[j+i+1];
                  }
                  String []arr_mid = new String[arr1.length -2];
                  for (int j = 1; j < arr1.length - 1; j++){
                      arr_mid[j - 1] = arr1[j];
                  }
                  for (int j = 0; j< arr_mid.length; j++){
                      if (arr_mid[j].equals(")")){
                          arr_mid[j] = "(";
                      } else{
                          arr_mid[j] = ")";
                      }
                  }
                  return "(" + solution(arr_to_s(arr2)) + ")" + arr_to_s(arr_mid);
              }
              }
              
              return p;
      }
  }
  ```

* String으로 풀이한 경우

  * 시간이 오래 걸림

  ```java
  class Solution {
      public String solution(String p) {
          if (p == ""){
              return p;
          }
  
          int a = 0;
          int b = 0;
          for (int i = 0;i < p.length();i++) {
              if (p.charAt(i) == '(') {
                  a += 1;
              } else {
                  b += 1;
              }
  
              if (b == a && p.charAt(0) == '(') {
                  String str1 = "";
                  String str2 = "";
                  for (int j = 0; j < i + 1; j++) {
                      str1 += p.charAt(j);
                  }
                  for (int j = 0; j < p.length() - i - 1; j++) {
                      str2 += p.charAt(j + i + 1);
                  }
                  return str1 + solution(str2);
              }
              if (a == b && p.charAt(0) == ')') {
                  String str1 = "";
                  String str2 = "";
                  for (int j = 0; j < i + 1; j++) {
                      str1 += p.charAt(j);
                  }
                  for (int j = 0; j < p.length() - i - 1; j++) {
                      str2 += p.charAt(j + i + 1);
                  }
                  String str_mid = str1.substring(1, str1.length() - 1);
                  String str_rev = "";
                  for (int j = 0; j < str_mid.length(); j++) {
                      if (str_mid.charAt(j) == '(') {
                          str_rev += ')';
                      } else {
                          str_rev += '(';
                      }
                  }
                  return "(" + solution(str2) + ")" + str_rev;
              }
          }
          return p;
      }
  }
  ```
  
  * 불필요한 과정 삭제 (최단시간 풀이)
  
  ```java
  class Solution {
      public String solution(String p) {
          if (p == ""){
              return p;
          }
  
          int a = 0;
          int b = 0;
          for (int i = 0;i < p.length();i++) {
              if (p.charAt(i) == '(') {
                  a ++;
              } else {
                  b ++;
              }
              if (b == a){
                  String str1 = "";
                  String str2 = "";
                  str1 = p.substring(0, i+1);
                  str2 = p.substring(i+1, p.length());
                  if (p.charAt(0) == '('){
                      return str1 + solution(str2);
                  } else{
                  String str_mid = str1.substring(1, str1.length() - 1);
                  String str_rev = "";
                  for (int j = 0; j < str_mid.length(); j++) {
                      if (str_mid.charAt(j) == '(') {
                          str_rev += ')';
                      } else {
                          str_rev += '(';
                      }
                  }
                  return "(" + solution(str2) + ")" + str_rev; 
                  }
              }
          }
          return p;
      }
  }
  ```