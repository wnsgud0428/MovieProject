# Subgroup3 Explain
- Subgroup3는 개봉 예정 영화 성공 예측 시스템 입니다.
- 사용자가 개봉 예정 영화에 대한 정보를 입력하고, 그 영화에 대한 성공 예측을 지원합니다.

## 클래스 다이어그램과의 구조 비교

1. Predict_params

- 웹에서 사용자로부터 입력을 받아옵니다.

2. Predictor
  
- 웹을 통하여 Predict_Params을 사용자로부터 받아와, Predictor class diagram에 있는 Predictor 함수를 통해 예측 결과를 출력합니다.
  
3. pageMaker

- Predict_Params를 바탕으로 사용자에게 영화 성공 예측 결과를 보여주는 페이지를 rendering합니다.

4. NewMovie Data

- Class diagram 구상 단계에서는 성공 예측을 하기 위해서 기존의 영화 데이터들을 DB에 저장해두고, 이를 바탕으로 성공 예측에 대한 기준을 정립하려 하였습니다. 하지만, 미리 Predict_params별 가중치를 따로 계산하고 가중치만 DB에 저장하는 방식을 채택하여 DB에 불필요한 데이터까지 저장하는 것을 피했습니다.

5. Checker

- Django의 forms 기능을 이용하여 Predict_params가 부족할 경우, 다시 입력을 받도록 하였습니다.

전체적으로 클래스 다이어그램과 일치하는 코드 구조를 제작하였습니다.

## 프로젝트 구체적 특징 

- 표본 데이터를 받아와 1차적으로 각 요소들(배우, 감독, 예산, 장르)별로 기준을 정해 데이터를 가공합니다. 가공한 데이터와 사용자가 웹에서 입력한 데이터를 각 요소별로 비교해 결과를 합산해, 합산한 결과의 수치에 따라 성공 구간을 판정하였습니다.

## 진행과정에서의 특별한 경험 및 어려웠던 점과 느낀 점

- NewMovie Data를 오픈 api를 통해 받아오고 DB에 저장하려 했으나, 찾아본 모든 API가 필요한 정보가(수익, 관객수, 누락된 데이터 다수) 부족하여 사용하지 못하였다. 그 결과로, 영화 정보를 받아와 분석하는 대신, 표본 데이터를 받아와 1차적으로 각 요소들(배우, 감독, 예산, 장르)별로 기준을 정해 데이터를 가공하는 방식으로 전환하였습니다.

- 데이터를 받아와 각 요소들을 가공하는 과정에서, 머신 러닝 모델을 이용해서 분석을 시도하였으나 앞서 말한 것처럼 관련 데이터들이 부족해서 정확도를 올리기 쉽지 않았고, 웹에 대한 지식도 부족하여 머신러닝 모델과 웹의 연결 문제로 인해 머신 러닝 모델 적용을 중단하였습니다. 

## 핵심 산출물과 얻은 경험

- 간단한 영화 성공 예측 웹 페이지이지만, DB - 웹(Django) - 파이썬 코드 로 이어지는 상호작용을 깨닫고 전체적인 개발의 한 과정을 경험한 것 같아 뜻깊었습니다. 또한 요구분석 단계부터 실제 구현까지 소포트웨어 공학의 큰 틀을 이해한 것 같아 귀중한 경험이였습니다.

## 사용예시
1. 영화 예측 메뉴 선택  
![image](https://user-images.githubusercontent.com/33649931/120145781-0ba3f000-c21f-11eb-882e-dcbe3e82a713.png)

---
2. 제작 예정 영화 정보 입력
   단, DB에 저장된 데이터(배우, 감독, 장르)와 일치하여야 정확도 계산에 도움이 된다.  
![2](https://user-images.githubusercontent.com/33649931/120146156-9dabf880-c21f-11eb-90c4-d29e07ade116.JPG)

---
3. 영화 성공 예측 결과 확인  
![3](https://user-images.githubusercontent.com/33649931/120146176-a69cca00-c21f-11eb-9c6b-9a417445406b.JPG)

---
4. 데모 영상  
![ezgif com-gif-maker](https://user-images.githubusercontent.com/33649931/120144708-65a3b600-c21d-11eb-9c76-1c54981ff20e.gif)

---
## 데이터 출처

 - 오픈 api 데이터를 사용하려 했으나 누락된 부분이 너무 많아 불가피하게 https://www.kaggle.com 의 데이터를 사용했습니다.
  
https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system/?select=tmdb_5000_credits.csv

https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system/?select=tmdb_5000_movies.csv

https://www.kaggle.com/therealsampat/predict-movie-success-rate?select=movie_success_rate.csv
