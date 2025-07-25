# 🤖 18 July 2025: Diving into OpenAI Agents SDK 🤖

This class was all about the core concepts you need to build smart AI agents. We covered how they "think," "remember," and how we can manage them.

---

## 💰 What are Tokens & How Much Do They Cost? 

Think of **tokens** as pieces of words. When you send a prompt to an AI or get a response, the length of that text is measured in tokens.

* **Pricing:** You pay based on the number of tokens you use (both for your input and the AI's output). It's like paying for data usage on your phone.
* **Token Counter:** Use OpenAI's [Tokenizer](https://platform.openai.com/tokenizer) to see how many tokens are in your text.

**Official Pricing Pages:**
* [OpenAI Pricing](https://openai.com/api/pricing/)
* [Google Gemini Pricing](https://ai.google.dev/gemini-api/docs/pricing)

---

## 🧠 Giving Your AI Context with RAG 

A **Retrieval-Augmented Generation (RAG)** system gives your AI long-term memory. Instead of only knowing what it was trained on, it can look up information in your personal documents to answer questions.

This involves two key parts:

### 1. Embeddings: Turning Words into Numbers
An **embedding** is a process that converts your text, images, or other data into a list of numbers called a **vector**. The cool part is that similar concepts will have similar numbers.
* `"Dog"` and `"Puppy"` will have very close vector numbers.
* `"Dog"` and `"Car"` will have very different vector numbers.

### 2. Vector Databases: The AI's Library 📚
A **vector database** is a special database designed to store these number lists (vectors). When you ask a question, the system first converts your question into a vector and then uses the database to find the most similar vectors from your documents. This is how it finds the most relevant information to answer your question.

We talked about two options:
* **OpenAI's built-in Vector Store**: Easy to use and integrated into their platform.
* **Pinecone**: A popular third-party vector database.

---

## 🛠️ How to Create a Vector Store on OpenAI 

You can easily create your own vector database (called a Vector Store) on the OpenAI platform to use with their **FileSearchTool**.

1.  Go to the [OpenAI Platform](https://platform.openai.com/).
2.  Navigate to **Dashboard** -> **Storage**.
3.  Click on **Vector Stores** -> **Create**.
4.  Give it a name and **upload** your files (like PDFs, text files, etc.).
5.  **Attach** the vector store to your agent.
6.  **Copy the Vector Store ID** and save it to use in your code! ✨

---

## 🕵️‍♀️ Tracing & Handoffs 

### Tracing: See How Your AI Thinks!
**Tracing** lets you see the step-by-step process an agent took to arrive at an answer. It's super useful for debugging and understanding what the AI is doing behind the scenes.
* You can view traces here: [OpenAI Traces](https://platform.openai.com/logs?api=traces)

### 🤝 Handoffs: Agent-to-Agent Teamwork 
A handoff is when one AI agent passes a task to another, more specialized agent. Think of it like a team where each member has a specific job. For example, a general "customer service" agent could hand off a complex technical question to a specialized "developer" agent to get the best possible answer.

---

## 🚀 Your Task for the Week 

Your mission for this week is to brainstorm an exciting product idea that you can build using AI agents. Once you have your idea, start planning and working on bringing it to life!

---

## Class Resources 🔗

* **Google Colab Notebook:** [Practice Notebook](https://colab.research.google.com/drive/1BE7dpOcGdLVqW5QIJaSrUrZfxSygMYFk?usp=sharing)
* **Class Code:** [GitHub Repository](https://github.com/syeda-hoorain-ali/giaic-q3/tree/main/class-11)
