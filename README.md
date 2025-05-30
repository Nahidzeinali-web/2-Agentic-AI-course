# 🚀 Getting Started with LangChain: Your First LLM App with OpenAI & Groq

If you're stepping into the world of Large Language Models (LLMs) and want to build apps that are **modular, composable**, and **production-ready**, then LangChain is your new best friend.

In this guide, I’ll walk you through a simple LangChain setup using OpenAI and Groq, with LangSmith for tracing.

---

## 📦 Step 1: Set Up Your Environment

We begin by loading our API keys and project settings securely using Python’s `dotenv`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

> ✅ Pro tip: Keep your `.env` file out of version control to avoid leaking secrets!

---

## 🤖 Step 2: Create Your First LLM Instance

Let’s create a language model instance using the OpenAI integration:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="o1-mini")
print(llm)
```

Now invoke it with a simple prompt:

```python
result = llm.invoke("What is Agentic AI?")
print(result.content)
```

LangChain makes this *deceptively easy* while keeping things extensible for more complex use cases.

---

## 🔄 Switching Models: Let’s Use Groq

Want to experiment with Groq's models? Just swap in the provider:

```python
from langchain_groq import ChatGroq

llm = ChatGroq(model="mixtral-8x7b-32768")
result = llm.invoke("Tell me a fun fact about AI")
print(result.content)
```

LangChain’s design makes switching backends seamless — no need to change your app logic.

---

## 🛠️ Why LangChain?

Here’s why I found LangChain worth using:

- **Unified Interface** for many LLM providers (OpenAI, Groq, Anthropic, etc.)
- **Integrated Tracing** via LangSmith for debugging and analysis
- **Chain and Agent building** that scales from quick scripts to production apps

---

## 🚀 What’s Next?

You’ve now taken your first steps with LangChain! From here, you can:

- Add memory to track conversations
- Use tools like web search or calculators with agents
- Build chains for document Q&A, summarization, and more

> Stay tuned — I’ll be sharing how to build multi-step LangChain agents with memory and vector search in my next post.

---

## 💬 Final Thoughts

LangChain lowers the barrier to building powerful AI apps, making it easier than ever to integrate LLMs into your workflows.

If you’ve tried LangChain, I’d love to hear how it’s working for you. Let me know in the comments or share your favorite use case! 👇
