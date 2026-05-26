# Git Push 오류 해결 요약

## 상황

- `git push origin main` 실행
- `non-fast-forward` 오류 발생
- 원격 저장소의 `main` 브랜치가 로컬보다 앞선 상태
- 로컬 커밋을 바로 push할 수 없는 상황

## 원인

- GitHub 원격 저장소에 로컬에 없는 커밋 존재
- 원격 변경사항을 먼저 가져와야 하는 상태
- 로컬 커밋과 원격 커밋의 이력 차이 발생

## 해결 흐름

### 1. 원격 변경사항 가져오기

```powershell
git pull --rebase origin main
```

- 원격 커밋 위에 로컬 커밋을 다시 적용하는 과정
- 일반적인 `merge` 커밋 없이 이력을 정리하는 방식

### 2. 충돌 상태 확인

```powershell
git status
```

- `interactive rebase in progress` 상태 확인
- `README.md` 파일 충돌 확인
- `both added: README.md` 메시지 확인

### 3. 충돌 파일 수정

- `README.md`의 충돌 표시 제거
- `<<<<<<<`, `=======`, `>>>>>>>` 구간 정리
- 필요한 README 내용만 남김
- 깨진 한글 문구 정상화

### 4. 충돌 해결 표시

```powershell
git add README.md
```

- 수정한 충돌 파일을 Git 인덱스에 반영
- 충돌 해결 완료 상태로 변경

### 5. rebase 계속 진행

```powershell
git rebase --continue
```

- 중단된 rebase 작업 재개
- 로컬 커밋 재생성
- 새 커밋 해시 생성

### 6. 상태 확인

```powershell
git status
git log --oneline --decorate -3
```

- 작업 트리 정리 상태 확인
- 최신 커밋 위치 확인
- `main` 브랜치 정상 상태 확인

### 7. 다시 push

```powershell
git push origin main
```

- rebase 완료 후 원격 저장소에 push
- 원격 이력과 로컬 이력이 맞춰진 상태에서 업로드

## 주의 사항

- `git push --force` 사용 지양
- 원격 저장소의 기존 커밋을 덮어쓸 수 있음
- 충돌 발생 시 파일 수정 후 `git add` 필요
- rebase 중단 시 `git rebase --abort` 사용 가능
- `.idea/` 파일은 필요 여부 확인 필요

## 최종 상태

- README 충돌 해결
- rebase 정상 완료
- 로컬 `main` 브랜치 정리
- 이후 `git push origin main` 실행 가능 상태
