## 실습 링크

[실습 링크](https://catalog.workshops.aws/sec4devs/ko-KR/)을 참고하세요

## 실습 내용에서의 변경 및 참고 사항

### 2. 릴리즈 자동화 - 프로젝트 파일 다운로드
- 처음 프로젝트를 시작할 때 Cloud9을 사용할 필요는 없습니다. pipeline 코드는 로컬에서 작업해도 충분합니다.
- 대신 CDK를 로컬에 설치해야 합니다. CDK는 node.js 런타임을 필요로 합니다. [설치 안내](https://docs.aws.amazon.com/ko_kr/cdk/v2/guide/getting_started.html)
- 서울 리전이 아닌, Amazon CodeGuru를 사용할 수 있는 리전에 배포해야 합니다. (버지니아 북부 등)

### 2. 릴리즈 자동화 - 파이프라인 및 도구 배포
- 프로젝트 파일은 CodeCommit을 사용하지 않고, S3 bucket을 사용하는 구성입니다.
- CodeCommit은 현재 deprecated 되어서, 기존 사용자가 아니라면 새로운 리포지토리를 생성할 수 없습니다.

### 4. Static Application Security Testing (SAST) - 코드 저장소 초기화
- 파이프라인 상에서 CodeCommit을 사용하지 않으므로, 소스코드의 변경 사항을 반영하려면 S3 bucket에 flask-app 프로젝트를 `flask-app.zip` 로 압축한 후 업로드해야만 합니다. (매우 번거롭습니다)
- 따라서, 기존의 CheckoutSource 스테이지의 S3Source 액션을 GitHub를 이용하는 것으로 변경하는 것을 추천합니다.
- GitHub에 repository를 생성한 후, flask-app 프로젝트의 모든 파일을 커밋/푸시하세요.
- 파이프라인 수정 화면에서, CheckoutSource 스테이지에 GitHub(버전 2)를 이용한 액션을 추가하세요. GitHub에 연결하는 과정이 필요합니다. (**아직 S3Source 액션을 지우지 마세요!**)
- 파이프라인 수정 화면에서, SAST, SCA, LicenseCheck, DockerBuild의 소스가 S3 bucket으로 되어 있는 것을 방금 생성한 GitHub 소스로 변경하세요.
- GitHub 소스로 변경이 끝나고 나면 S3Source 액션을 지우고, 최종적으로 파이프라인을 저장합니다.
- flask-app git repository의 `sast_buildspec.yaml` 파일의 내용을 바꿔주어야 합니다. [링크](https://github.com/gotoweb/flask-app-devsecops/blob/main/sast_buildspec.yaml)를 참고하세요.
- 이후, GitHub의 push 트리거에 의해 파이프라인이 작동하는 것을 확인하세요.
- GitHub 연결을 위해 파이프라인의 IAM Role 수정이 필요합니다. 파이프라인이 사용하는 IAM Role에서, CodeStar Connections 권한(`arn:aws:codestar-connections:::*`)을 허용해줍시다.

### 4. Static Application Security Testing (SAST) - True Positives 표시
- 우리 파이프라인은 SonarQube를 사용하지 않습니다. 대신 Amazon CodeGuru Reviewer를 사용합니다. 모든 결과는 _\[Amazon CodeGuru Reviewer - 코드 검토 - 전체 리포지토리 분석\]_ 에서 확인할 수 있습니다.
