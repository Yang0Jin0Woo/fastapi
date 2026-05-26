# fastapi

## FastAPI 실행 방법

Windows PowerShell 기준입니다.

### 1. 가상환경 만들기

```powershell
python -m venv .hello_fastapi
```

### 2. 가상환경 활성화

```powershell
.hello_fastapi\scripts\activate
```

활성화되면 프롬프트 앞에 `(.hello_fastapi)`가 표시됩니다.

### 3. FastAPI 설치

```powershell
pip install "fastapi[standard]==0.128.0"
```

### 4. 애플리케이션 실행

```powershell
fastapi dev main.py
```

실행 후 브라우저에서 아래 주소를 열어 확인합니다.

```text
http://127.0.0.1:8000
```

API 문서는 아래 주소에서 확인할 수 있습니다.

```text
http://127.0.0.1:8000/docs
```
