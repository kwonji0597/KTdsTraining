# 🚀 KTdsTraining - RAG 기반 Travel Assistant Demo

Azure OpenAI Service + Azure AI Search 기반의 **Retrieval-Augmented Generation (RAG)** 예제 프로젝트입니다.

본 프로젝트는 **Margie's Travel Assistant** 라는 가상 시나리오로 구성되어 있으며:

✅ **콘솔 기반 인터페이스**  
✅ **Streamlit 기반 웹 인터페이스**  

→ 두 가지 버전으로 구현되어 있습니다.

---

## 📦 사용 기술

- Python 3.x
- Azure OpenAI Service (Chat API)
- Azure AI Search (Vector Search 적용)
- python-dotenv (환경변수 관리)
- Streamlit (웹 UI)
- Visual Studio Code + GitHub 연동

---

## 📁 프로젝트 구조

```
KTdsTraining/
├── .gitignore
├── .env.example
├── README.md
├── 00.RAG.app.py # 콘솔 기반 RAG Assistant
├── 01.rag_chat.py # Streamlit 기반 RAG Assistant (웹 UI)
└── requirements.txt # 필수 패키지 리스트
```


---

## 🚀 실행 방법

### 1️⃣ GitHub에서 프로젝트 클론

```bash
git clone https://github.com/kwonji0597/KTdsTraining.git
cd KTdsTraining
```

### 2️⃣ 가상환경 생성 (선택)
```
python -m venv .venv
.\.venv\Scripts\activate    # Windows
# source .venv/bin/activate # Mac/Linux
```
### 3️⃣ 필수 패키지 설치
```
pip install -r requirements.txt
```

### 4️⃣ 환경변수 설정 (.env 파일 생성)
```
# .env 예시

OPENAI_ENDPOINT=https://xxxxx.openai.azure.com
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CHAT_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-ada-002
SEARCH_ENDPOINT=https://xxxxx.search.windows.net
SEARCH_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
INDEX_NAME=your-index-name
```
주의: .env 파일은 GitHub 에 절대 push 하지 않도록 .gitignore 에 포함되어 있습니다.


---
# 실행 예제
## ✅ 콘솔 기반 실행
```
python 00.RAG.app.py
```

Streamlit 웹 인터페이스 실행
```
streamlit run 01.rag_chat.py

```
---
### ✅ 주요 기능
RAG (Retrieval-Augmented Generation) 적용

Azure AI Search 에서 벡터 기반 검색 적용

최신 문서 기반으로 답변 생성

Chat Memory 유지 (대화 흐름 유지)

Streamlit 기반 채팅 인터페이스 제공

대화 내용 히스토리 지원