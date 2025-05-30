
# 🚀 Getting Started with LangChain: Your First LLM App using OpenAI & Groq

LangChain lets you build **modular**, **composable**, and **production-ready** applications powered by Large Language Models (LLMs). Whether you're a researcher or a developer, this guide will help you build your first LLM app using **OpenAI**, **Groq**, and **LangSmith** for tracing.

---

## 📚 Table of Contents

1. [Set Up Your Environment](#-step-1-set-up-your-environment)
2. [Create Your First LLM Instance](#-step-2-create-your-first-llm-instance)
3. [Switching Models with Groq](#-switching-models-lets-use-groq)
4. [Why LangChain?](#️-why-langchain)
5. [Ingesting Files & Web Data](#-ingesting-text-pdfs-webpages-and-arxiv-papers-with-langchain)
6. [Chunking Long Documents](#-how-to-use-recursivecharactertextsplitter-in-langchain-to-chunk-large-documents)
7. [Next Steps](#-final-thoughts)

---

## 📦 Step 1: Set Up Your Environment

Start by loading your environment variables safely using `dotenv`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

> 💡 **Pro Tip**: Never push `.env` files to GitHub. Add them to your `.gitignore` for safety.

---

## 🤖 Step 2: Create Your First LLM Instance

Let’s create an LLM using **OpenAI**:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")
print(llm)
```

And invoke it with a simple prompt:

```python
result = llm.invoke("What is Agentic AI?")
print(result.content)
```

> 🧠 **LangChain simplifies LLM usage** by abstracting provider differences behind a consistent API.

---

## 🔄 Switching Models: Let’s Use Groq

You can easily switch to **Groq** models with a simple change:

```python
from langchain_groq import ChatGroq

llm = ChatGroq(model="mixtral-8x7b-32768")
result = llm.invoke("Tell me a fun fact about AI")
print(result.content)
```

> 🔄 No need to refactor — just change the class name. Your app logic stays the same.

---

## 🛠️ Why LangChain?

Here’s why LangChain stands out:

✅ **Unified LLM Interface** – OpenAI, Groq, Anthropic, HuggingFace, etc.  
✅ **Powerful Tracing & Debugging** – with LangSmith  
✅ **Composable Chains & Agents** – build from quick tests to enterprise apps

---

# 📄 Ingesting Text, PDFs, Webpages, and arXiv Papers with LangChain

LangChain’s **Community Loaders** make ingesting content effortless. You can process everything from `.txt` and `.pdf` files to websites and scientific papers.

---

## 📘 1. Loading `.txt` Files

```python
from langchain_community.document_loaders.text import TextLoader

loader = TextLoader('speech.txt')
text_documents = loader.load()
```

✅ Great for transcripts, logs, or any plain-text input.

---

## 📄 2. Reading PDF Files

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('syllabus.pdf')
docs = loader.load()
```

Each page is parsed into a separate `Document`. Ideal for academic or scanned files.

---

## 🌐 3. Loading Web Pages

Basic usage:

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_paths=["https://python.langchain.com/docs/"])
docs = loader.load()
```

With BeautifulSoup filtering:

```python
import bs4

loader = WebBaseLoader(
    web_paths=["https://lilianweng.github.io/posts/2023-06-23-agent/"],
    bs_kwargs={"parse_only": bs4.SoupStrainer(class_=("post-title", "post-content"))}
)

docs = loader.load()
```

> 🧼 Only load the good parts: avoid footers, ads, and navbars.

---

## 📚 4. Ingesting arXiv Papers

```python
from langchain_community.document_loaders import ArxivLoader

docs = ArxivLoader(query="quantum computing", load_max_docs=2).load()
```

> 🧪 Perfect for building research agents or summarizing recent studies.

---

## 🔍 Summary Table of Loaders

| Loader Type   | Module/Class          | Use Case                          |
|---------------|------------------------|-----------------------------------|
| `.txt`        | `TextLoader`           | Notes, logs                       |
| `.pdf`        | `PyPDFLoader`          | Contracts, syllabi, reports       |
| Web URL       | `WebBaseLoader`        | Web articles, blogs, docs         |
| arXiv         | `ArxivLoader`          | Academic paper ingestion          |

---

# 🧠 How to Use `RecursiveCharacterTextSplitter` to Chunk Large Documents

LLMs have a context limit — you can’t pass a full book! That’s where **chunking** helps.

---

## 📄 Step 1: Load Your PDF Document

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('syllabus.pdf')
docs = loader.load()
```

---

## ✂️ Step 2: Apply Recursive Splitting

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

final_documents = text_splitter.split_documents(docs)
```

> 🧠 Recursive strategy splits at paragraph > sentence > word > character to preserve meaning.

---

## 🔍 Sample Output

```python
print(final_documents[0])
```

Each `Document` chunk has:

- Clear, logical text segmentation  
- Metadata (source, page number, etc.)  
- Overlapping text to retain context

---

## ✅ Why Use RecursiveCharacterTextSplitter?

✅ Smarter chunking preserves meaning  
✅ Works better than naive sentence splitters  
✅ Ideal for embedding, summarization, or Q&A tasks

---

## 🚀 Final Thoughts

LangChain gives you powerful building blocks to create AI pipelines. From model invocation to ingesting content and chunking it smartly — **this is how you productionize LLMs**.

---

> 🔜 **Coming up**: Learn how to embed your document chunks using FAISS and run similarity searches with LangChain.

Stay tuned!
