# 5-4

## 개발서버옵션

- python manage.py runserver
  - 서버가 bind되는 아이피는 디폴트로 127.0.0.1
  - 각 OS마다 127.0.0.1 주소는 localhost 도메인에 디폴트 매핑
- 네트워크를 통해 같은 네트워크의 다른 컴퓨터에서 접속하려면?
  - 0.0.0.0을 지정하여 모든 아이피에대해 접속을 받을 수 있도록 설정이 필요
    - `python manage.py runserver 0.0.0.0:8000`
- 그리고 외부망에서 접속하려면 외부 네트워크 설정도 필요.

- 실제로 해보니 토큰설정도 필요함
- `ngrok authtoken tokens`
- `ngrok http httpport`
  - 설정을하면 외부 네트워크에서 해당 주소로 접속이 가능하다
  - 개발용서버