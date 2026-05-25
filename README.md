# 🧠 Antigravity Agent Builder (powered by Google ADK)

This repository contains the standard development template and specifications for building custom single-agents and multi-agent teams using the **Antigravity SDK (Google Agent Development Kit - ADK)**.

---

## 🏛️ Project Structure

- `agent_builder.py`: Standalone Python script demonstrating single-agent tool definition and orchestrator multi-agent routing.
- `SKILL.md`: The official interactive `agent-builder-helper` skill file used by the Antigravity agent to co-create custom agents through a back-and-forth (Tiki-Taka) workflow.

---

## 🚀 How to Get Started

### 1. Requirements
Ensure you have the Google GenAI SDK and ADK installed:
```bash
pip install google-genai
# (And other Google ADK dependencies configured in your environment)
```

### 2. Set Up API Key
Configure your Gemini API key in your environment variables:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

### 3. Run the Agent
Run the script to test the Multi-Agent team:
```bash
python agent_builder.py
```

---

## 🔄 Interactive Tiki-Taka Workflow

The `SKILL.md` defines a structured workflow where the AI assistant:
1. **Asks** for the agent's goals and parameters (APIs, SQL queries, or file formats).
2. **Refines** the python docstrings (tools) and system instruction prompts.
3. **Generates** the complete Python script based on this repository's template.
