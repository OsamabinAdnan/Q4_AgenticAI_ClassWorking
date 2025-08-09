@everyone 

# **🤖 8 August 2025: Diving into OpenAI Agents SDK 🤖**
Today we learned how to run our own code at specific moments in an agent's process using **Lifecycle Hooks** and how to adjust the AI model's behavior with **Model Settings**.
~~-------------------------------------~~

## ⏰ Lifecycle Hooks: Running Code at the Right Time 
**Lifecycle Hooks** are functions that you can set up to run automatically at key moments in your agent's life. Think of them as custom triggers that give you control over the agent's process.

There are two main types:
* **Agent Hooks**: This focuses on the individual agent. It lets you inject custom logic right into the agent's specific workflow—tracking events such as when an agent starts processing, when it completes its task, and when it interacts with external tools.
    * **Code Example**: [Agent Lifecycle Code](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/19_agent_lifecycle)

* **Run Hooks**: This manages global events that span the entire execution or "run" of one or more agents. It allows you to monitor and control overarching events such as the start and end of an agent's execution, tool invocations, and handoffs between agents.
    * **Code Example**: [Run Lifecycle Code](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/18_run_lifecycle)
~~-------------------------------------~~

## 🎛️ Model Settings: Control Your AI Agent Brain
You can control how the AI model generates responses by adjusting its settings. This lets you adjust its personality and performance. For example:
* **Temperature:** How creative vs. focused your agent is
* **Tool Choice:** Whether your agent can use calculators, weather apps, etc.
* **Max Tokens:** How long the response can be
* **Parallel Tools:** Whether your agent can use multiple tools at once

* **Code Example**: [Model Settings Code](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/07_model_settings)