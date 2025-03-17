# Django

## 0. setting
- '.gitignore'
- 가상환경 설정
    - 가상환경 실행: python -m venv venv
    - 가상환경 설치: source venv/Scripts/activate
- 'README.md'

## 1. Django 프로젝트

1. django 설치
```shell
pip install django
```

2. 프로젝트 생성
```
django-admin startproject <pjt-name> <path>
```

3. 서버 실행(종료: 'ctrl + c')
```
python manage.py runserver runserver
```

4. 앱 생성
```shell
django-admin startapp <app-name>
```

5. 앱 등록 (`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    '<app-name>'
]
```

# 프로잭트 폴더(first_pjt)는 모든 앱들을 통합 관리
# 앱 폴더(first_app)는 독립적으로 관리되는 폴더