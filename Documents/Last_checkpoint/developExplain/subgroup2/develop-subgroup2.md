# Subgroup2 Explain
- Subgroup2는 영화 개인화 추천 시스템 입니다.
- 사용자가 일정 개수 이상의 영화를 평가하고, 적절한 영화를 추천 받습니다.

## 클래스 다이어그램과의 구조 비교

1. userChecker(class diagram)

- subgroup1의 구현 내용이기 때문에 생략하였음. (이 상태에서는 이미 userChecker를 통해 사용자 정보는 받아온 상태임.)

- user정보가 있는 것으로 가정하고 구현함.

2. controller 및 movieRecommender
  
- MovieRecView은 storage에서 사용자의 영화 평가 정보와 전체 영화정보를 가져오고, 영화 추천 리스트를 생성한다.
  
3. pageMaker

- 2번에서 생성된 영화 추천 리스트를 가지고, 사용자에게 영화 추천 리스트를 보여주는 페이지를 rendering한다.

4. storage
- allMovie(모든 영화 정보)와 allUserMovieEvalData(유저가 영화평가를 남겼던 정보)가 db.sqlite3에 저장되어있음.
- movieRecommender class 에서 getAllMovieData()와 getUserMovieEvalData() 를 사용하여 위의 db에 저장된 데이터들을 가져갈 수 있음.


전체적으로 클래스 다이어그램과 일치하는 코드 구조를 제작하였습니다.

## 사용예시
  
1. 영화 추천 메뉴 선택

![20210529_231335_1](https://user-images.githubusercontent.com/33649857/120073841-05096180-c0d5-11eb-8e8c-e29dd3307252.png)  
---  

2. 영화 평가하러 가기 (영화 추천을 받으려면, 사용자의 영화 평가 데이터가 필요)

![20210529_231335_2](https://user-images.githubusercontent.com/33649857/120073844-09ce1580-c0d5-11eb-9473-195dc484953b.png)
---  

3. 영화 평가 및 추천 받는 화면 (영화 평가 화면에서는 랜덤으로 10개의 영화 목록을 보여줌)

![222](https://user-images.githubusercontent.com/33649857/120073942-7f39e600-c0d5-11eb-9f9d-133b13a74a10.gif)
