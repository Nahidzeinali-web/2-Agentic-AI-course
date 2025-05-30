
# 📄 LangChain Document Loaders and Text Splitters – A Practical Guide

LangChain supports multiple document loaders and text splitting strategies for preprocessing various types of data. This guide includes examples for loading text, PDF, web content, Arxiv, and Wikipedia, as well as different text splitting techniques.

---

## 📚 Table of Contents

- [1. Document Loaders](#1-document-loaders)
  - [Text Loader](#text-loader)
  - [PDF Loader](#pdf-loader)
  - [Web Page Loader](#web-page-loader)
  - [Arxiv Loader](#arxiv-loader)
  - [Wikipedia Loader](#wikipedia-loader)
- [2. Text Splitters](#2-text-splitters)
  - [RecursiveCharacterTextSplitter](#recursivecharactertextsplitter)
  - [CharacterTextSplitter](#charactertextsplitter)
  - [HTMLHeaderTextSplitter](#htmlheadertextsplitter)
  - [RecursiveJsonSplitter](#recursivejsonsplitter)

---

## 1. Document Loaders

### Text Loader
```python
from langchain_community.document_loaders.text import TextLoader

loader = TextLoader("speech.txt")
text_documents = loader.load()
```

### PDF Loader
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("syllabus.pdf")
docs = loader.load()
```

### Web Page Loader
```python
from langchain_community.document_loaders import WebBaseLoader
import bs4

loader = WebBaseLoader(
    web_paths=["https://lilianweng.github.io/posts/2023-06-23-agent/"],
    bs_kwargs={"parse_only": bs4.SoupStrainer(class_=["post-title", "post-content", "post-header"])}
)
docs = loader.load()
```

### Arxiv Loader
```python
from langchain_community.document_loaders import ArxivLoader

docs = ArxivLoader(query="1706.03762", load_max_docs=2).load()
```

### Wikipedia Loader
```python
from langchain_community.document_loaders import WikipediaLoader

docs = WikipediaLoader(query="Generative AI", load_max_docs=4).load()
```

---

## 2. Text Splitters

### RecursiveCharacterTextSplitter

Split text by paragraphs, then sentences, then words. Ideal for generic documents.
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
final_documents = text_splitter.split_documents(docs)
```

### CharacterTextSplitter

Simple method that splits by character (e.g., `\n\n`).
```python
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=100, chunk_overlap=20)
split_docs = text_splitter.split_documents(docs)
```

### HTMLHeaderTextSplitter

Splits HTML documents based on structure like h1, h2, h3.
```python
from langchain_text_splitters import HTMLHeaderTextSplitter

html_string = """<html><body><h1>Foo</h1><p>Intro</p>...</body></html>"""
headers_to_split_on = [("h1", "Header 1"), ("h2", "Header 2"), ("h3", "Header 3")]

html_splitter = HTMLHeaderTextSplitter(headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)
```

### RecursiveJsonSplitter

Splits large nested JSON objects by character size limit.
```python
import requests
from langchain_text_splitters import RecursiveJsonSplitter

json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
json_splitter = RecursiveJsonSplitter(max_chunk_size=300)
json_chunks = json_splitter.split_json(json_data)
```

---

These tools help you preprocess data efficiently before sending to a language model. They support chunking large documents and maintaining semantic structure for better LLM performance.
