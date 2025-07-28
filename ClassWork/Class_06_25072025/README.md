# **🤖 25 July 2025: Diving into OpenAI Agents SDK 🤖**

Today we covered how to control and provide memory to our AI agents using **Guardrails** and **Context**.

---

## 🛤️ Guardrails: Keeping Your Agent on Track

**Guardrails** are rules you set to control an agent's behavior, ensuring its inputs and outputs are appropriate.

* **Input Guardrails**: Check the user's message *before* it goes to the agent to filter or block content.
* **Output Guardrails**: Check the agent's response *before* it's sent to the user to ensure quality and safety.

---

## 🤔 Context: What Your Agent Knows

**Context** is the information an agent has available to perform its tasks.

* **Local Context**: Temporary information available for just agent loop in the conversation.
* **Agent/LLM Context**: The agent's main "memory" that persists across turns. This includes:
    * The **System Prompt** (its core instructions).
    * The **User's Prompts**.
    * Its available **Custom Tools**.
    * Information from **Retrieval** or a **Web Search**.

---

## ⚠️ Important Model Note

The `gemini-2.0-flash` model **cannot** use **Tool Calling** and **Structured Output** in the same agent. To achieve this, you must either use two separate agents or choose a different model that supports both features simultaneously.

---

## 📚 Homework

Dive deeper into these concepts for our next session:

* **Learn more about Context**: [https://openai.github.io/openai-agents-python/context/](https://openai.github.io/openai-agents-python/context/)
* **Learn about Dynamic Instructions**: [https://openai.github.io/openai-agents-python/agents/#dynamic-instructions](https://openai.github.io/openai-agents-python/agents/#dynamic-instructions)

---

## 📗 Class Code

* **GitHub Repository:** [https://github.com/syeda-hoorain-ali/giaic-q3/tree/main/class-12](https://github.com/syeda-hoorain-ali/giaic-q3/tree/main/class-12)

