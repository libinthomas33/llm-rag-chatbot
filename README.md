# Simple Company Policy Chatbot

This project implements a company policy chatbot using LangChain and RAG. The chatbot assists employees with questions about company policies and procedures by providing instant responses based on the retrieved documents from a vector database.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/libinthomas33/llm-rag-chatbot.git
cd llm-rag-chatbot
```
### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Usage
Place your company policy documents in the data/ directory.

Set your OpenAI API key in the script with your actual API key.
```bash
python3 chat.py
```
Interact with the chatbot in the terminal. Type your questions and get responses based on the company policies. 

To exit, type `q`

