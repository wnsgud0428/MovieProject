

# 서브 그룹 별 코드 실행 방법



## 0-1. Tech Stack

- Python
- Django Framework
- Html, CSS


## 0-2. Subgroup Explain
- 각 서브 그룹 별 Source Code는 각각의 브랜치를 생성하여 관리하고 있습니다.(ex: 서브 그룹 1 => subgroup1 branch)
  
- 각 서브 그룹 별 코드 설명 및 마지막 체크포인트 관련 문서들은 main 브랜치에서 관리중입니다.


 
---

### 아래와 같은 공통적인 절차를 통해 각 브랜치에서 서브그룹 code를 독립적으로 실행할 수 있습니다.

---
## 1. install virtual environment

```
 pip install pipenv
```

## 2. install requirement 
```
pipenv install
```

## 3. activate virtual environment

```
pipenv shell
```

## 4. run server

```
python manage.py runserver
```