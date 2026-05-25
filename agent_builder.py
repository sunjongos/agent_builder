from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import os
import asyncio

# Model configuration
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-pro")

# 1. Define tools for the agent
def get_patient_visit_count(patient_name: str) -> str:
    """환자의 최근 내원 횟수를 조회하는 도구 (도수치료 횟수 체크용)"""
    print(f"[Tool] Querying database for patient: {patient_name}")
    # Mock database retrieval
    return f"{patient_name} 환자는 이번 달 총 3회 도수치료를 받았습니다."

# 2. Define the sub-agents
billing_helper = Agent(
    name="billing_helper",
    model=MODEL,
    description="환자 내원 정보 및 도수치료 횟수를 조회하고 관리하는 요원",
    instruction="""당신은 병원 행정 및 청구 관리 에이전트입니다.
    환자의 내원 횟수 확인 요청이 들어오면 반드시 'get_patient_visit_count' 도구를 사용하여 확인한 후,
    정중하게 안내해 주세요.""",
    tools=[get_patient_visit_count]
)

document_writer = Agent(
    name="document_writer",
    model=MODEL,
    description="정량 보행 보고서 데이터를 참조하여 실손 청구 소명서를 자동 작성하는 요원",
    instruction="환자의 보행 불균형 데이터를 근거로 보험사 제출용 소명 문서를 품격 있게 작성하세요."
)

# 3. Define the main orchestrator (Multi-Agent Team Routing)
hospital_orchestrator = Agent(
    name="hospital_orchestrator",
    model=MODEL,
    description="대표 병원 실무 지원 마스터 사령관",
    instruction="""당신은 병원 실무 지원 팀의 총괄 팀장입니다.
    들어오는 요청의 성격에 따라 알맞은 요원에게 임무를 전달(Routing)하세요.
    - 환자 진료 이력/횟수 조회 건 -> billing_helper 요원에게 전달
    - 실손보험 소명서 및 문서 작성 건 -> document_writer 요원에게 전달""",
    sub_agents=[billing_helper, document_writer]
)

# 4. Asynchronous run execution
async def run_agent_team(user_prompt: str):
    session_service = InMemorySessionService()
    runner = Runner(
        agent=hospital_orchestrator,
        app_name="hospital_management_app",
        session_service=session_service,
    )
    
    session = await session_service.create_session(
        app_name="hospital_management_app", 
        user_id="luca_director"
    )
    
    new_message = types.Content(
        role="user", 
        parts=[types.Part.from_text(text=user_prompt)]
    )
    
    print(f"\n💬 Request: {user_prompt}")
    print("🤖 Agent Response: ", end="", flush=True)
    
    async for event in runner.run_async(
        user_id="luca_director", 
        session_id=session.id, 
        new_message=new_message
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, "text") and part.text:
                    print(part.text, end="", flush=True)
    print("\n" + "="*50)

if __name__ == "__main__":
    # Test execution
    asyncio.run(run_agent_team("홍길동 환자가 이번 달에 도수치료 몇 번 받았는지 조회해 줘"))
