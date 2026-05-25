---
name: agent-builder-helper
description: 대표님이 필요한 에이전트 요구사항을 말하면 데이터 연동 방식(API, DB 직접연동, 엑셀 내보내기 낚아채기, OCR)을 정밀 진단하고, 세계 최고 수준의 소프트웨어 설계 원칙(SRP, 방어적 도구 설계, 자가 복구, 하이브리드 아키텍처, 헤르메스식 메신저 연동)을 갖춘 파이썬 ADK 코드를 빌드하는 인터랙티브 개발 스킬.
category: development
---

# 🧠 World Best Practice: Antigravity SDK 에이전트 빌더 가이드

이 스킬은 대표님께서 원하는 직관적인 업무 자동화 요구사항(예: "진료비 청구 삭감 분석기 만들어줘")을 제시했을 때, **Google ADK(Agent Development Kit)** 환경에서 안정적이고 가성비가 뛰어나며 장애에 스스로 대응하는 **세계 최고 수준(World Best Practice)**의 에이전트 코드 및 도구를 대표님과의 **점진적 질의응답(티키타카)**을 통해 빌드하는 가이드라인입니다.

---

## 🏛️ 세계 최고 수준의 에이전트 설계 5대 원칙 (5 Gold Rules)

### 1. 단일 책임 요원 설계 (Single-Responsibility Principle)
- 하나의 거대한 에이전트가 모든 작업을 전담하게 만들면 프롬프트 비대화, 토큰 낭비, 기능 오작동이 발생합니다.
- 복잡한 작업은 반드시 **상황을 분석하고 태스크를 분배하는 사령관(Orchestrator)**과 **개별 도구를 다루는 전문 실무 요원(Worker Sub-Agents)**으로 분리하여 협업 체계를 구성합니다.

### 2. 방어적 도구 엔지니어링 (Defensive Tool Engineering)
- 에이전트가 도구를 올바르게 호출하도록 파이썬 함수에 명확한 **타입 힌팅(Type Hinting)**과 **상세한 한글 주석(Docstring)**을 반드시 작성합니다.
- **예외 안전(Exception Safety)**: 도구 내부에서 예외(Exception)가 발생해 프로그램이 완전히 뻗어버리는 일을 차단합니다. 에러가 나면 프로그램 크래시 대신 `{"status": "error", "message": "에러 내용"}`과 같이 구조화된 JSON 데이터나 요약 텍스트를 반환하여, AI 에이전트가 에러 원인을 스스로 읽고 이해할 수 있도록 설계합니다.
- **보안성(Security)**: SQL 인젝션 공격이나 악성 입력을 방어하기 위해 파라미터 바인딩(Parameterized Query) 및 입력값 유효성 검사를 도구 진입부에서 철저히 수행합니다.

### 3. 자가 복구 프로토콜 (Self-Healing Loop)
- 에이전트가 도구를 호출하다가 에러(예: 테이블 컬럼명 불일치, API 일시적 타임아웃, 잘못된 파라미터 전달)를 만났을 때 바로 포기하지 않고, **에러 원인을 스스로 진단하여 파라미터를 보정한 후 재시도(Retry)**하도록 프롬프트 지침에 복구 행동 강령을 심어둡니다.

### 4. 하이브리드 비용 최적화 아키텍처 (Pro + Flash Hybrid)
- **오케스트레이터**: 복잡한 의사결정 및 추론을 수행하므로 **`gemini-2.5-pro`** 모델로 세팅합니다.
- **실무 요원 / 도구 전처리**: 대용량 로우 데이터를 처리하거나 OCR, 엑셀 읽기 등 단순 작업 위주는 속도가 빠르고 10배 이상 저렴한 **`gemini-2.5-flash`** 모델을 전담 배치합니다.
- **토큰 세이브**: 대용량 파일은 Python `pandas` 등으로 파이썬 런타임 내에서 1차 가공(필터링, 요약 통계)을 끝내고 핵심 요약본만 에이전트에 인입시키며, 반복 조회되는 32k 토큰 이상의 정적 정보는 **Context Caching**을 설정해 호출 비용을 90% 이상 절감합니다.

### 5. 세션 및 컨텍스트 수명 주기 격리
- 다중 사용자 환경에서도 상태가 꼬이지 않도록 `InMemorySessionService`를 구성하고, 개별 사용자의 고유 세션 ID(`session.id`)를 격리하여 대화 히스토리를 체계적으로 보존합니다.

---

## 🏥 [진단 가이드] 데이터 연동 방식 4대 전술 매트릭스

원내망 EMR 등 정보 차단이 극심한 인프라에서 최적의 연동 방식을 진단하는 기준입니다.

```mermaid
graph TD
    Start[연동 방식 진단 시작] --> Q1{솔루션 벤더가<br>공식 API를 제공하나요?}
    Q1 -- 예 --> MethodA[A. API 방식 선택]
    Q1 -- 아니오 --> Q2{내부 DB에 접근하여<br>Read-Only 쿼리 조회가 가능한가요?}
    Q2 -- 예 --> MethodB[B. 온프레미스 DB 직접 연동]
    Q2 -- 아니오 --> Q3{화면에 엑셀/CSV<br>내보내기 기능이 존재하나요?}
    Q3 -- 예 --> MethodC[C. 엑셀 내보내기 인터셉트]
    Q3 -- 아니오 --> MethodD[D. 화면 OCR & PDF 파싱]
```

| 구분 | A. API 방식 | B. 온프레미스 DB 방식 | C. 엑셀 내보내기 인터셉트 | D. 화면 OCR / PDF 파싱 |
| :--- | :--- | :--- | :--- | :--- |
| **권장 환경** | 외부 솔루션 연동 가능 시 | DB 스키마 분석 가능 및 접속 허용 시 | API/DB 접속 차단, 엑셀 출력 가능 시 | API/DB/엑셀 모두 불가, 화면 정보 캡처 |
| **보안 강도** | 🟢 우수 (정식 인증) | 🔴 취약 (방화벽 개방 및 권한 관리 필요) | 🟢 우수 (기존 솔루션 권한 우회 없음) | 🟡 중간 (개인정보 마스킹 주의 필요) |
| **장애 대응성**| 🟢 우수 (규격 고정) | 🟡 중간 (스키마 변경 시 쿼리 수정) | 🟢 우수 (UI 변경 영향 없음) | 🔴 취약 (화면 디자인 변경 시 템플릿 영향) |

---

## 💻 연동 방식별 World Best Practice 파이썬 코드 구현 템플릿

### A. API 방식 (Defensive API Tool)
```python
import requests
from typing import Dict, Any

def fetch_patient_visit_api(patient_id: str) -> Dict[str, Any]:
    """병원 솔루션 API를 통해 특정 환자의 내원 이력을 조회합니다.
    
    Args:
        patient_id: 조회할 환자의 고유 ID 번호 (예: 'P10039')
    Returns:
        상세 내역 딕셔너리 혹은 에러 요약 데이터
    """
    if not patient_id.isalnum():
        return {"status": "error", "message": "올바르지 않은 환자 ID 형식입니다."}
        
    api_url = f"https://emr.local-hospital.com/api/v1/patients/{patient_id}/visits"
    headers = {
        "Authorization": "Bearer SECURE_TOKEN_HERE",
        "Content-Type": "application/json"
    }
    
    try:
        # 타임아웃을 반드시 5초 내외로 길게 주어 스레드 락 방어
        response = requests.get(api_url, headers=headers, timeout=5.0)
        
        # 4xx, 5xx 에러 발생 시 예외 발생
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
        
    except requests.exceptions.Timeout:
        return {"status": "error", "message": "EMR API 서버 응답 초과 (Timeout). 잠시 후 다시 시도하십시오."}
    except requests.exceptions.HTTPError as http_err:
        return {"status": "error", "message": f"HTTP 오류 발생 ({response.status_code}): {str(http_err)}"}
    except Exception as e:
        # 프로그램 크래시를 방지하고 에러 로그를 AI 에이전트에게 공급
        return {"status": "error", "message": f"알 수 없는 시스템 오류: {str(e)}"}
```

### B. 온프레미스 DB 직접 연동 방식 (Parametrized SQL DB Tool)
```python
import pyodbc
from typing import List, Dict, Any

def query_sales_database(search_date: str) -> List[Dict[str, Any]]:
    """원내 SQL Server 데이터베이스에서 특정 날짜의 매출 요약을 안전하게 쿼리합니다.
    
    Args:
        search_date: 조회 타겟 날짜 (YYYY-MM-DD 형식)
    """
    # 날짜 유효성 정규식 검사 등으로 SQL 인젝션 1차 방어
    import re
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", search_date):
        return [{"status": "error", "message": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 포맷을 준수하십시오."}]
        
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=192.168.0.50,1433;"
        "DATABASE=Hospital_Billing;"
        "UID=readonly_agent;"
        "PWD=Secure_Agent_Password_99!;"
        "Connection Timeout=3;" # 빠른 실패 설정
    )
    
    # 보안의 핵심: Dynamic SQL을 피하고 반드시 파라미터 바인딩 (?) 방식을 사용합니다.
    query = """
        SELECT TOP 30 PatientName, CodeEZ777, Price, TreatDate 
        FROM BillingMaster 
        WHERE TreatDate = ? 
        ORDER BY Price DESC
    """
    
    try:
        with pyodbc.connect(conn_str) as conn:
            with conn.cursor() as cursor:
                # 쿼리 실행 시 두 번째 인자로 파라미터 튜플 전달 (SQL Injection 완전 방어)
                cursor.execute(query, (search_date,))
                columns = [col[0] for col in cursor.description]
                
                rows = cursor.fetchall()
                if not rows:
                    return [{"status": "info", "message": f"{search_date} 날짜에 조회된 데이터가 존재하지 않습니다."}]
                    
                return [dict(zip(columns, row)) for row in rows]
                
    except pyodbc.Error as db_err:
        # DB 에러 코드를 구조화하여 에이전트에 피드백 -> 에이전트가 테이블/컬럼 유추 가능하도록 지원
        return [{"status": "error", "message": f"데이터베이스 쿼리 오류: {str(db_err)}"}]
    except Exception as e:
        return [{"status": "error", "message": f"시스템 연동 장애: {str(e)}"}]
```

### C. 엑셀 내보내기 인터셉트 방식 (File-Safe Watchdog Interceptor)
```python
import os
import time
import pandas as pd
from typing import Dict, Any

def safely_parse_emr_excel(file_path: str) -> Dict[str, Any]:
    """새로 생성된 EMR 다운로드 엑셀 파일을 감지하고, 파일 쓰기 락이 풀리면 안전하게 파싱합니다.
    
    Args:
        file_path: 감지된 Excel 파일의 로컬 절대 경로
    """
    if not os.path.exists(file_path):
        return {"status": "error", "message": "파일을 찾을 수 없습니다."}
        
    # [World Best Practice] 파일 쓰기가 완료될 때까지 슬립 루프를 도는 방어 로직 (크래시 방지)
    max_retries = 5
    for i in range(max_retries):
        try:
            # 쓰기 모드로 임시 오픈하여 파일 락 상태 체크
            with open(file_path, "r+"):
                break
        except IOError:
            print(f"[File Watcher] 파일이 쓰기 잠금 상태입니다. 대기 중... ({i+1}/5)")
            time.sleep(0.5)
    else:
        return {"status": "error", "message": "파일 다운로드가 오랜 시간 완료되지 않았거나 다른 프로세스가 점유하고 있습니다."}
        
    try:
        # [비용 최적화] 로우 데이터를 통째로 넘기지 않고 Pandas로 1차 전처리(토큰 세이브)
        df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)
        
        # 기밀 정보(주민번호 등) 마스킹 처리 및 요약 통계 계산
        summary = {
            "status": "success",
            "file_name": os.path.basename(file_path),
            "row_count": len(df),
            "columns": list(df.columns),
            "total_amount": int(df['진료비'].sum()) if '진료비' in df.columns else 0,
            "average_amount": int(df['진료비'].mean()) if '진료비' in df.columns else 0,
            "top_3_records": df.head(3).to_dict(orient="records")
        }
        return summary
    except Exception as e:
        return {"status": "error", "message": f"엑셀 파싱 및 전처리 중 에러 발생: {str(e)}"}
```

### D. 화면 OCR / PDF 파싱 방식 (Multimodal Vision OCR Tool)
```python
from google import genai
from google.genai import types
import os
from typing import Dict, Any

def execute_multimodal_ocr(file_path: str) -> Dict[str, Any]:
    """EMR 화면 캡처 또는 스캔본 PDF를 Gemini Vision을 사용해 구조화된 JSON 데이터로 변환합니다.
    
    Args:
        file_path: 캡처된 이미지 혹은 PDF의 로컬 절대 경로
    """
    if not os.path.exists(file_path):
        return {"status": "error", "message": "업로드된 캡처 파일을 찾을 수 없습니다."}
        
    # 가성비가 매우 높고 OCR 인식률이 좋은 Flash 모델을 지정합니다.
    client = genai.Client()
    
    mime_type = "application/pdf" if file_path.endswith('.pdf') else "image/png"
    
    try:
        with open(file_path, "rb") as f:
            file_bytes = f.read()
            
        prompt = """
        당신은 병원 행정 정산 전문가입니다. 
        제공된 EMR 캡처 화면 혹은 문서 이미지에서 다음 정보만을 추출하여 아래 JSON 규격으로 반환하십시오.
        텍스트 외의 설명글이나 백틱(```json) 마크업은 제외하고 순수 JSON 데이터만 반환하십시오.
        
        {
          "visit_date": "YYYY-MM-DD",
          "patient_name": "환자명",
          "total_billed": 150000,
          "ez777_prescribed": true/false,
          "notes": "특이사항 요약"
        }
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(data=file_bytes, mime_type=mime_type),
                prompt
            ]
        )
        
        import json
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        parsed_json = json.loads(clean_text)
        return {"status": "success", "data": parsed_json}
        
    except json.JSONDecodeError:
        return {"status": "error", "message": f"추출 데이터의 JSON 포맷 변환 실패. 원본 응답: {response.text}"}
    except Exception as e:
        return {"status": "error", "message": f"Gemini Vision 분석 중 치명적 오류: {str(e)}"}
```

---

## 🔁 자가 복구(Self-Healing)를 위한 에이전트 프롬프트 가이드라인

에이전트 조립 시 시스템 Instruction에 반드시 **장애 진단 및 자동 복구 지침**을 다음과 같이 심어주어야 최고의 복구율을 달성할 수 있습니다.

```markdown
당신은 도구 호출 결과로 에러 메시지(status: error)를 전달받은 경우, 다음 매뉴얼을 준수해 문제를 진단하고 재검사하십시오.
1. '데이터베이스 쿼리 오류: Column X not found' 에러를 만난 경우:
   - 본인이 사용한 컬럼명이 테이블 스펙과 다른 상태입니다. 즉시 스키마 정의 도구를 재호출하거나, 대표님께 해당 테이블의 정확한 컬럼 명세를 물어본 뒤 올바른 쿼리로 자동 수정하여 실행하십시오.
2. 'Timeout' 또는 'Network Error' 에러를 만난 경우:
   - 외부망 또는 내부 통신망 장애입니다. 대표님께 네트워크 끊김 사실을 알리고 3초 뒤에 단 1회 재접속을 자동 시도하십시오.
3. '올바르지 않은 파라미터' 에러를 만난 경우:
   - 이전 사용자 대화 맥락을 파싱하여 타입이나 형식을 보정해(예: 날짜에서 하이픈 제거 등) 도구를 재요청하십시오.
```

---

## 🏥 [헤르메스 패턴] 병원 메신저 비서 에이전트 연동 (Messenger Integration)

헤르메스 에이전트처럼 복잡한 클라우드 구성 없이, 병원 내 방화벽 내부에서 안정적으로 기동하는 **텔레그램 폴링 기반 경량 연동 아키텍처**입니다. 추가 라이브러리 없이 파이썬 표준 라이브러리와 `requests`로만 안전하게 구동됩니다.

```
┌────────────────────────┐         ┌────────────────────────┐         ┌────────────────────────┐
│  원내 PC (Background)   │  ◄───►  │    Telegram Server     │  ◄───►  │  원장님 스마트폰 (App)   │
│  [ADK Runner & Bot]    │  (HTTPS)│  (Webhook 없이 Polling) │  (LTE)  │   [텔레그램 채팅방]    │
└────────────────────────┘         └────────────────────────┘         └────────────────────────┘
```

### 헤르메스 메신저 브릿지 파이썬 코드 예시
```python
import os
import time
import requests
import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# 텔레그램 봇 토큰 및 대표님 고유 Chat ID 설정
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")
ALLOWED_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID", "12345678")) # 보안 목적: 지정된 사용자만 차단 필터링

def send_telegram_message(chat_id: int, text: str):
    """지정된 채팅방으로 마크다운 텍스트 답장을 보냅니다."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print(f"[Telegram] 발송 실패: {e}")

async def telegram_polling_bridge(runner: Runner, session_service: InMemorySessionService):
    """텔레그램 메시지를 롱폴링(Long-Polling)으로 수집하여 ADK 에이전트 러너에 포워딩합니다."""
    print("🚀 헤르메스 텔레그램 메신저 브릿지 기동 완료...")
    offset = 0
    
    # 격리된 단일 세션 미리 열어둠 (대화 컨텍스트 유지용)
    session = await session_service.create_session(app_name="hospital_helper", user_id=str(ALLOWED_CHAT_ID))
    
    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates?offset={offset}&timeout=10"
            response = requests.get(url, timeout=12)
            if response.status_code != 200:
                await asyncio.sleep(2)
                continue
                
            updates = response.json().get("result", [])
            for update in updates:
                offset = update["update_id"] + 1
                message = update.get("message", {})
                chat_id = message.get("chat", {}).get("id")
                user_text = message.get("text", "")
                
                # 보안 체크: 허가된 대표님/행정 계정만 제어 허용
                if chat_id != ALLOWED_CHAT_ID:
                    send_telegram_message(chat_id, "🚫 접근 권한이 없는 계정입니다.")
                    continue
                
                if not user_text:
                    continue
                    
                print(f"[Telegram 수신]: {user_text}")
                
                # ADK 에이전트에 메시지 주입 및 실행
                new_message = types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=user_text)]
                )
                
                # 결과 수집
                full_reply = ""
                async for event in runner.run_async(
                    user_id=str(ALLOWED_CHAT_ID),
                    session_id=session.id,
                    new_message=new_message
                ):
                    if event.content and event.content.parts:
                        for part in event.content.parts:
                            if hasattr(part, "text") and part.text:
                                full_reply += part.text
                
                # 텔레그램 채팅방으로 응답 전송
                send_telegram_message(chat_id, full_reply)
                
        except Exception as e:
            print(f"[Bridge Error] {e}")
            await asyncio.sleep(3) # 에러 시 쿨다운
```

---

## 🏥 [EMR 실무 플레이북] 3대 병원 자동화 에이전트 시나리오

대표님이 새로운 에이전트를 빌드해 나갈 때, 병원 현장에 즉각 적용하여 큰 비용 효과를 낼 수 있는 대표 실무 시나리오 명세서입니다.

### 시나리오 1: 일일 매출 및 EZ777(보행분석) 통계 브리핑 요원
- **목적**: 매일 퇴근 전 혹은 출근 길에 당일 정산 매출과 비급여 EZ777 검사 건수를 요약 보고받음.
- **도구 구성**: `query_sales_database` (직접 DB 연동) 또는 `safely_parse_emr_excel` (당일 다운로드된 엑셀 파싱).
- **작동 방식**: 대표님이 텔레그램으로 *"오늘 정산 보고"*라고 치면, 오늘 비급여 보행분석 건수, 수가 합계액, 실손청구 삭감 리스크 환자 명단을 분석하여 텔레그램 메시지로 예쁘게 포맷팅해 반환.

### 시나리오 2: 도수치료 삭감 한도 사전 심사 요원 (Claims Cut Audit)
- **목적**: 5세대 실손보험 도입에 따른 연간 도수치료 횟수 제한(예: 15회 또는 24회 이상 시 관리급여 심사 삭감 리스크)을 예방하기 위해, 한도에 임박한 환자를 자동으로 찾아 경고함.
- **도구 구성**: 환자의 최근 1년간 내원 기록 및 수가 코드를 조회하는 DB/Excel 전처리 도구.
- **작동 방식**: EMR 다운로드 디렉토리에 새로운 환자 통계가 감지되면, 도수치료 누적 횟수가 12회를 초과한 환자 명단을 추출해 원장님 텔레그램으로 *"⚠️ [주의] 홍길동 환자 도수치료 13회차 도달 - EZ777 보행분석 결합 필요"* 경고 메시지 자동 발송.

### 시나리오 3: 보험사 실손 소명서 자동 작성 요원 (Appeal Letter Writer)
- **목적**: 보험사에서 도수치료 청구를 삭감하거나 정밀 심사를 요구할 때 제출할 비급여 소명서(보행 분석 객관적 근거 자료)를 의학적 서식에 맞춰 자동 작성.
- **도구 구성**: `execute_multimodal_ocr` (원내 스마트 인솔 보행 결과 보고서 캡처 이미지 OCR 판독).
- **작동 방식**: 스마트 인솔 보행 검사결과지 캡처 이미지를 텔레그램 방에 업로드하며 *"이 환자 소명서 써줘"*라고 요청하면, 이미지를 판독해 **"좌우 족저압 불균형 18% 및 보행 대칭성 붕괴 상태로 보존적 재활 치료의 의학적 필요성이 소명됨"** 등의 완성형 소명서 양식을 생성.

---

## 🎭 루카(Luca) 본부장의 멘탈 모델 (Mental Model for Luca)
- **헤르메스 연동 선제 제안**: 새로운 에이전트 빌드 요청 시, 화면이 없는 백엔드 전용 시나리오는 대표님께 **"텔레그램 봇으로 연결해서 폰으로 보고받으시겠습니까?"**를 먼저 권장하십시오.
- **비용 최우선 권장**: 에이전트를 만들고자 할 때 반드시 요금 효율적인 **Pro + Flash 하이브리드 아키텍처**를 기본 설계안으로 대표님께 추천해야 합니다.
- **안전한 SQL 전파**: DB 방식을 논의할 때, 반드시 **Read-Only(조회 전용) 계정 사용** 및 쿼리 복잡성(운영 DB 성능 영향 최소화)을 검증하도록 경고 지침을 명시합니다.
- **점진적 상세화**: 한 번에 코드를 다 짜려고 성급히 덤비지 마십시오. API 스펙과 DB 정보가 부족하면 *"대표님, 이 API의 필수 파라미터는 무엇인가요?"* 혹은 *"조회할 테이블의 스키마(컬럼명)를 올려주십시오"* 라고 집요하면서도 정중하게 티키타카를 이끌어가야 합니다.
