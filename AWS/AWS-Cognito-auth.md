## AWS Cognito와 인증 서비스들에 대해서 알아보기

##### AWS Cognito?
- add user sign-up and sign-in to mobile / web apps. 
- Features
    - User Pools : 
        - Create & maintain user directory & add sign-up / sign-in to mobile app or web application.
        - Use 3rd-party identity providers (Google, Facebook, AMazon, SAML-based identity providers)
        - Enhanced security features, MFA
    - Federated Identities:
        - Create unique identities for users & authenticate them with federated identity providers.
        - obtain temporary, limited-privilege AWS credentials to synch data with Cognito Sync.
        - Supports developer authenticated identities.
        - Register & authenticate users via your own backend authentication systems
    - Cognito Sync : supports offline access & cross device syncing

##### 유저 관리 앱 만들기 - step by step
- https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3
- https://medium.com/@kangzeroo/user-management-with-aws-cognito-2-3-the-core-functionality-ec15849618a4
- https://medium.com/@kangzeroo/user-management-with-aws-cognito-3-3-last-steps-to-full-fledged-73f4a3a9f05e

- 내용 간단 요약:
    1. 코그니토 서비스에 접속하여 유저 풀을 생성
    2. attributes, policies, 인증 방법, 인증 메세지, 디바이스 등등 관련 설정들을 진행 (상세는 추후 추가)
    3. Federal Identities 설정 - 한 사용자에 대해서 여러개의 3rd party 로그인 서비스를 사용하고 싶을 때 사용
    4. Federal Identities에 원하는 provider들 등록
    5. Cognito SDK를 이용해서 앱(프론트쪽)에서 호출, 가입, 인증, 로그인 등을 처리
    6. 유저 정보 수정, 패스워드 분실, 자동 로그인, 백엔드 인증(이거에 대해선 좀 더 살펴볼 필요 있음) 등 까지 모두 처리 가능