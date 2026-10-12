# NCP NKS DevOps Lab

NCP 기반 Kubernetes 배포·운영·자동화 학습 프로젝트입니다.

## 환경

- NKS Kubernetes v1.36.2 / Worker 2대
- NCP Container Registry
- NCP ALB + Gateway API
- nginx 애플리케이션

## 검증한 내용

- NCR 이미지 push 및 private image pull
- HPA CPU 부하에 따른 3 → 5 → 6개 확장
- v1 배포,  v2 롤링배포
- PDB를 준수한 앱 Pod 선택적 drain
- 두 노드에 Pod 분산 배치
- Public ALB를 통한 HTTP 접속
- Secret Manager CSI 연동 및 일반 Secret으로 전환

## 저장소 구조

- app/: Dockerfile과 웹 페이지
- gitops/apps/nginx-web/: 앱 배포·자동 확장·중단 보호
- gitops/infra/gateway/: ALB와 라우팅 설정
- docs/: 구성·검증·장애 해결 문서

## 사전 조건

- 관련 Gateway API 및 NCP Add-on이 설치된 NKS
- web-app 네임스페이스
- 별도 생성한 ncr-local-secret 이미지 pull Secret
- 환경에 맞는 NCR 주소와 Public LB 서브넷 설정

인증정보와 Secret 원문은 저장소에 포함하지 않습니다.
현재 Dockerfile은 기존 NCR nginx-lab:v1 이미지에 의존합니다.

## 진행 예정

- GitHub Actions CI
- Argo CD GitOps 배포
- 모니터링·알림
- IaC와 운영 자동화
