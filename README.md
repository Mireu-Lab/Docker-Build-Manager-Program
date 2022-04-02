# Hosting Project 

1. 기본 프로그램 리스트

- docker

- pip-fastapi
- pip-docker

2. API Install

해당 API는 파이썬 Fastapi을 이용하여 호스트을 진행합니다.
프로그램을 실행하기 앞써 해당프로그램은 **리눅스 우분투 기반으로 개발이 되었습니다**

API 설치는 아래와 같이 진행 하십시오

```sh
cd  Install
sudo sh install.sh
```

설치가 되었으면 아래와 같이 프로그램을 실행 하십시오

```sh
cd App
sudo python3 main.py
```

해당 프로그램은 관리자 권한으로 실행을 해야하는 프로그램입니다
관리자 권한 없는 계정으로 실행시 도커 빌드중에 권한부족으로 에러가 출력됩니다

3. API Docs

해당 API는 Fastapi로 이루어져 보안 솔루션 및 여러 플랫폼을 넣을수있게 설계을 하였습니다

> 127.0.0.1:8080/<br>
    매인 페이지

> 127.0.0.1:8080/container/build<br>
    설명 : 도커 컨테이너 빌드<br>
    원하는 데이터 : name<br>

> 127.0.0.1:8080/container/start<br>
    설명 : 도커 컨테이너 시작<br>
    원하는 데이터 : name<br>

> 127.0.0.1:8080/container/stop<br>
    설명 : 도커 컨테이너 정지<br>
    원하는 데이터 : name<br>

> 127.0.0.1:8080/container/kill<br>
    설명 : 도커 컨테이너 강제정지<br>
    원하는 데이터 : name<br>

> 127.0.0.1:8080/container/remove<br>
    설명 : 도커 컨테이너 삭제<br>
    원하는 데이터 : name<br>

> 127.0.0.1:8080/container/info<br>
    설명 : 도커 컨테이너 정보<br>
    원하는 데이터 : name<br>

4. API Set

API는 사용자가 쉽게 조작할수있게 설계되어있으며
몇개의 코드와 소스만 넣는다면 배포 가능하게 설계되어있습니다

해당 배포 프로그램은 [도커 허브][https://hub.docker.com]에 이미지을 올려서 이미지을 받아 배포하는 형식으로 개발이 되어있습니다

현제 기본 세팅으로 배포해주는 프로그램은 우분투에 주피터 랩을 설치 한 이미지을 배포 하게 설계 되었습니다

배포 하시고 싶은 이미지가있으면 **/App/dply/build.py**에서 코드을 추가 하시면 됩니다 
해당프로그램은 [Docker SDK]["https://docker-py.readthedocs.io/"]기반으로 만들어졌으니 확인 하면서 개발 하시기 바랍니다
