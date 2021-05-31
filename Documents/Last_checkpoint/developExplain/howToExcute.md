

# 서브 그룹 별 코드 실행 방법



## 0-1. Tech Stack

- Python 3.9
- Django Framework 2.2.5
- Html5, bootstrap CSS


## 0-2. Subgroup Explain
- 각 서브 그룹 별 Source Code의 경로는 다음과 같습니다.

MovieProject/Develop/Subgroup#num_dev
  
- 각 서브 그룹 별 코드 설명 및 마지막 체크포인트 관련 문서 경로는 다음과 같습니다.

MovieProject/Documents/Last_checkpoint


 
---

### 아래와 같은 공통적인 절차를 통해 각 브랜치에서 서브그룹 code를 독립적으로 실행할 수 있습니다.

---
## 1. Git clone
```
git clone https://github.com/wnsgud0428/MovieProject.git
```


## 2. Install Virtual Environment

```
 pip install pipenv
```

## 3. Directory Change (to develop)
```
cd develop/subgroup1_dev
```

## 4. Install Requirement 
```
pipenv install
```

## 5. Activate Virtual Environment

```
pipenv shell
```

## 6. Run Server

```
python manage.py runserver
```
