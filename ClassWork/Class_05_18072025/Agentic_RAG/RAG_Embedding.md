# 📘 Briefing: The Art of RAG – Core Components and Workflow

This is a simple overview of how **RAG (Retrieval-Augmented Generation)** works. RAG is a powerful method where AI looks up useful information before answering questions. It combines three key parts:

1. **Embedding**
2. **Retrieval**
3. **LLM (Large Language Model)**

---

## 🔢 1. Embedding – Turning Data into Vectors

- **What is embedding?**  
  It's the process of converting files like PDFs, audio, or text into **vectors** (numbers) that represent their meaning.

- **Why use vectors?**  
  Similar ideas or emotions are turned into vectors that are **close together** in the vector space.  
  > Example: If someone says “Acha” four times in a movie scene, each with different emotion, the vector will capture that change.

- **Important Note:**  
  GPT-4.0 is **not used** for embedding. There are **special models** for this.

- **Where do we store them?**  
  In a **vector database** like [Pinecone](https://www.pinecone.io), which is designed to store and search vectors efficiently.

---

## 🔎 2. Retrieval – Finding the Right Information

- **Step 1: Convert the prompt into a vector**  
  When the user asks a question, the system also turns that question into a vector.

- **Step 2: Search for similar vectors**  
  The system looks in the vector database for the most **relevant or similar** content.

- **Step 3: Convert back to readable text**  
  The system turns those matching vectors back into **text** that the LLM can use.

- **Tools:**  
  You can either:
  - Build your own retrieval system using Python, or  
  - Use a ready-made tool like **FileSearch Tool**.

---

## 🤖 3. LLM – Generating Smart Responses

- The LLM receives:
  - The **original question**, and  
  - The **content** retrieved from the vector database.

- Then it **writes a detailed, accurate answer**, based on this up-to-date information.

---

## 🔁 Summary of Workflow

```text
1. Convert original data (e.g. PDF, audio) into vectors with emotions.
2. Store these vectors in a vector database.
3. User sends a prompt to the agent.
4. The prompt is also converted into a vector.
5. The system searches for similar vectors in the database.
6. Found vectors are turned back into text and send back to retrival system.
7. Both the prompt and text are sent to the LLM from retrival system.
8. The LLM generates a helpful response.
9. We can either make retrival system of our own or use a tool like FileSearch Tool.
10. In OpenAI SDK, FileSearchTool is retrival system in this RAG process/workflow.
```