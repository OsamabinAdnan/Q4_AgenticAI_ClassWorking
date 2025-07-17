# Agentic AI - Streaming Examples using Gemini API

This project contains two Python scripts that demonstrate the use of the [`agents`](https://github.com/ai-collection/agents) framework with **Google Gemini API** via OpenAI-compatible endpoints. It showcases how to run streaming chat completions and integrate tool/function calling using agents.

---

## 📁 Files Overview

### ✅ `main.py` - Streaming Response from Gemini Agent
A simple example of streaming a large text response from Gemini using an agent.

- Uses Gemini model (`gemini-2.0-flash`)
- Streams a long-form response to a user query (e.g., "Tell me about Agentic AI in 1000 words")

### ✅ `streaming.py` - Agent with Tool Use + Streaming
A more advanced example that integrates function/tool calling:

- The agent first calls a function `how_many_jokes()` to determine how many jokes to generate
- Then, it generates that many jokes
- Output is streamed event-by-event

---

## 📦 Requirements

- Python 3.10+
- `agents` library
- `openai`
- `python-dotenv`

You can install dependencies via:

```bash
pip install -r requirements.txt
```