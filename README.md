## 👗 Triple S



### 📋 프로젝트 정보

- 팀명 : 재.향.뿌.
- 팀장 : 김재호
- 팀원 : 길민규, 김준기, 심동식, 정다솜
- 프로젝트 : 코디에 따른 향수 추천으로 3S (Scent, Style, Sense) 완성
- 기간 : 2020.10.12 ~ 2020.11.13

<br />

### 💡 Local 실행

#### FrontEnd

```
$ npm install
$ npm run serve
```

#### BackEnd

```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```



<br />



### 💡 팀원 정보 및 역할 분담

| 팀원   | 역할 | 비고                        |
| ------ | ---- | --------------------------- |
| 김재호 | 팀장 | FE / BE, Jira관리           |
| 길민규 | 팀원 | FE / BE, 전체적인 UI/UX     |
| 김준기 | 팀원 | FE / BE, 추천 알고리즘 구현 |
| 심동식 | 팀원 | FE / BE, AWS, AI            |
| 정다솜 | 팀원 | FE / BE, DB 모델링 및 관리  |



<br />



### 💡 목표 서비스 구현 및 실제 구현 정도

#### 목표 서비스

* 이미지에서 사람 인식(image segmentation), 스타일 분석 결과(adjective)에 따라 어울리는 향수 추천
* 데이터 크롤링 및 Open API 활용
* HTML, CSS, JavaScript, Vue.js, Django, REST API, MariaDB 등을 활용한 실제 서비스 설계
* Python, Pandas, Numpy 등을 활용한 데이터 정제 및 추천 알고리즘 구현
* AWS, EC2를 활용한 서비스 배포 및 관리



#### 실제 구현도

- Vue.js 와 Django REST Framework를 활용한 서비스 설계

- [향수](https://www.fragrantica.com/) 데이터 크롤링을 통해 데이터 전처리 및 정제

- 추천 알고리즘 구현

  - 연령별 어울리는 향수 추천(진행 중)

  - 날씨 API를 활용한 계절/날씨별 어울리는 향수 추천(진행 중)
  - 이미지를 통해 사람 인식(image segmentation), 스타일 분석 결과(adjective)에 따라 어울리는 향수 추천(진행 중)

- HTML, CSS, JS을 활용한 UI/UX



<br />



### 💡 개발 환경

##### Frontend (Vue.js)

- axios
- bootstrap
- bootstrap-vue
- JWT
- vue
- vue-cookies
- vue-router

##### Backend (Django REST API 서버)

- Django
- Django REST framework
- Python
- pandas
- numpy
- Keras(Tensorflow)
- OpenCV

##### DB

* MariaDB

##### 서비스 배포 환경

- Linux
- Nginx
- Gunicorn



<br />



### 💡 기능

#### Accounts

- 유저 프로필

#### Perfumes

- 30개 이상의 브랜드의 향수 리스트

#### Styles

* 