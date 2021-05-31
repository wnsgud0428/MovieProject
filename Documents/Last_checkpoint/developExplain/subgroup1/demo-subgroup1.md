# Subgroup1 Explain
- Subgroup1은 로그인 및 화원가입 시스템 입니다.
- 사용자가 회원가입때 등록한 아이디, 이메일과 비밀번호를 입력하면 사이트에 로그인됩니다.

## 클래스 다이어그램과의 구조 비교

1. information checker & controller(class diagram)

- information checker : Django.contrib.auth의 클래스 views 안에 있는 as_view() 함수를 통해 사용자가 입력한 아이디와 비밀번호를 db에 있는 전체 사용자의 아이디와 비밀번호와 대조하여 일치하는 정보가 있으면 사용자의 로그인을 허용하고 그렇지 않으면 접근을 제한한다.

2. user data storage
  
- 현재까지 회원가입한 사용자의 아이디와 비밀번호가 db.splite3 파일에 저장되어있다.
  
3. pageMaker

- 로그인과 회원가입을 하기 위한 페이지를 rendering한다.


전체적으로 클래스 다이어그램과 일치하는 코드 구조를 제작하였습니다.


## 사용예시
  
시작 페이지로 로그인하지 않았을때는 아무 기능도 사용할 수 없습니다.

![image](https://user-images.githubusercontent.com/33653264/120108685-49623380-c1a1-11eb-8c40-0b60279a0d68.png)
---  

로그인 버튼을 눌렀을때 (1)등록된 user 정보를 입력하거나 (2) 회원가입을 할 수 있습니다.

![image](https://user-images.githubusercontent.com/33653264/120108878-02c10900-c1a2-11eb-9a9d-6c4e078cc89e.png)
---  

회원가입 창에서는 (1) 새로운 user 정보를 입력하여 회원가입을 하거나 (2) 다시 로그인 화면으로 돌아갈 수 있습니다.

![image](https://user-images.githubusercontent.com/33653264/120109812-022a7180-c1a6-11eb-8368-f1770089ad81.png)
---

회원가입을 하게 되면 해당 user정보로 로그인 되고 user name과 사용할 수 있는 기능들이화면에 표시됩니다.
(로그아웃을 다시 누르면 로그인 전 상태로 돌아가게 됩니다.)

![image](https://user-images.githubusercontent.com/33653264/120109819-08205280-c1a6-11eb-843b-781c76e77e6d.png)
---

마지막으로 관리자 화면에서는 moving에 가입된 모든 user들을 확인 할 수 있습니다.

![image](https://user-images.githubusercontent.com/33653264/120109825-0ce50680-c1a6-11eb-83d6-9dcc4ebdfd66.png)
---

Demo 영상

![bandicam 2021-05-31 00-07-05-434](https://user-images.githubusercontent.com/33653264/120109778-dc04d180-c1a5-11eb-93e7-438370fa2280.gif)
---


