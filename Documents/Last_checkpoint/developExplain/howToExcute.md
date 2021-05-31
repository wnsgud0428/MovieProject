

# 서브 그룹 별 코드 실행 방법



## 0-1. Tech Stack

- Python 3.9
- Django Framework 2.2.5
- Html5, bootstrap CSS


## 0-2. Subgroup Explain
- 각 서브 그룹 별 Source Code는 각각의 브랜치 내의 develop폴더에서 관리하고 있습니다.(ex: 서브 그룹 1 => subgroup1 branch)
  
- 각 서브 그룹 별 코드 설명 및 마지막 체크포인트 관련 문서들은 main 브랜치에서 관리중입니다.


 
---

### 아래와 같은 공통적인 절차를 통해 각 브랜치에서 서브그룹 code를 독립적으로 실행할 수 있습니다.

---
## 1. Git clone
```
git clone https://github.com/wnsgud0428/MovieProject.git
```

## 2. Pull the branch you want to execute. 
```
git pull origin subgroup1(or subgroup2 or subgroup3)
```


## 3. Install Virtual Environment

```
 pip install pipenv
```

## 4. Directory Change (to develop)
```
cd develop
```

## 5. Install Requirement 
```
pipenv install
```

## 6. Activate Virtual Environment

```
pipenv shell
```

## 7. Run Server

```
python manage.py runserver
```
