
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


# 🧠 LangChain Agentic AI Tutorial

This guide walks through setting up LangChain with environment variables, invoking different models, chaining prompts, and parsing outputs into various formats like JSON, XML, and YAML using Pydantic.

---

## 🔐 1. Loading Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()
```

### Retrieve environment variables:
```python
os.getenv("LANCHAIN_PROJECT")
os.getenv("LANGCHAIN_API_KEY")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

---

## 💬 2. Using OpenAI and Groq LLMs

```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="o1-mini")
print(llm)
print(llm.invoke("What is Agentic AI").content)
```

```python
from langchain_groq import ChatGroq
model = ChatGroq(model="qwen-qwq-32b")
response = model.invoke("Hi, my name is Nahid")
print(response)
```

---

## 🧠 3. Prompt Engineering with Templates

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert AI Engineer. Provide me answer based on the question"),
    ("user", "{input}")
])
```

---

## 🔗 4. Chaining Prompt with Model

```python
model = ChatGroq(model="gemma2-9b-it")
chain = prompt | model
response = chain.invoke({"input": "Can you tell me something about Langsmith"})
print(response.content)
```

---

## 🔄 5. Output Parsing

### Text Parsing
```python
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()
chain = prompt | model | output_parser
response = chain.invoke({"input": "Can you tell me about Langsmith"})
print(response)
```

### JSON Parsing
```python
from langchain_core.output_parsers import JsonOutputParser
output_parser = JsonOutputParser()
prompt = PromptTemplate(
    template="Answer the user query:\n{format_instruction}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instruction": output_parser.get_format_instructions()}
)
```

### XML Parsing
```python
from langchain_core.output_parsers import XMLOutputParser
output_parser = XMLOutputParser()
```

---

## 🧱 6. Structured Outputs with Pydantic

### Using Pydantic
```python
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

parser = JsonOutputParser(pydantic_object=Joke)
```

---

## 📦 7. YAML Output with Pydantic

```python
from langchain.output_parsers import YamlOutputParser

parser = YamlOutputParser(pydantic_object=Joke)
```

---

## 🎯 8. Final Assignment – Product Assistant

### Define Schema
```python
class ProductInfo(BaseModel):
    product_name: str = Field(..., description="The name of the product")
    product_details: str = Field(..., description="A brief description of the product")
    tentative_price_usd: int = Field(..., description="Tentative price in USD as an integer")
```

### Create Prompt + Chain
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that provides product information."),
    ("user", "{input}\n{format_instructions}")
])
prompt = prompt.partial(format_instructions=output_parser.get_format_instructions())

model = ChatGroq(model="gemma2-9b-it")
chain = prompt | model | output_parser

response = chain.invoke({"input": "Tell me about the Apple MacBook Air"})
print(response)
```

---

This complete workflow demonstrates how to:
- Load and use API keys securely.
- Use LangChain-compatible LLMs.
- Design prompts.
- Build chaining workflows.
- Parse responses into structured formats.

