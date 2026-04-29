# Financial RAG Bot

## Project Overview

Financial RAG Bot is an AI-powered trading assistant built using Retrieval-Augmented Generation (RAG) principles.

The goal of this project is to combine:

* Trading and finance knowledge from books/PDFs
* Live stock market data
* Technical indicators (RSI, EMA, Trend)
* Local LLM reasoning using Llama 3 via Ollama

and generate:

* BUY / SELL / HOLD decisions
* Confidence level
* Explanation of reasoning
* Risk awareness

This is not just a chatbot. It is a decision-focused AI trading assistant.

---

# Final Goal

The objective was to build a system that can answer questions like:

**"Is TCS good for swing trading right now?"**

and return:

```text
Decision: BUY / SELL / HOLD
Confidence: LOW / MEDIUM / HIGH
Reason:
- Why this decision was made
Risk:
- Main risk factor
```

instead of generic AI answers.

---

# Tech Stack

## LLM

* Llama 3 (via Ollama)

## Embeddings

* sentence-transformers
* all-MiniLM-L6-v2

## Vector Database

* ChromaDB

## Stock Market Data

* yFinance (Yahoo Finance)

## Language

* Python

## Environment

* Windows + Virtual Environment (venv)

---

# Folder Structure

```text
financial-rag-bot/
│
├── data/
│   ├── pdfs/
│   │   ├── Zerodha Varsity PDFs
│   │   └── Other trading books
│   │
│   ├── extract_all.py
│   ├── clean.py
│   ├── raw_combined.txt
│   ├── filtered.txt
│   ├── knowledge.txt
│   └── stock.py
│
├── db/
│   └── ChromaDB persistent vector database
│
├── embeddings/
│   └── store.py
│
├── indicators/
│   └── indicators.py
│
├── rag/
│   ├── retrieve.py
│   └── llm.py
│
├── venv/
│
└── main.py
```

---

# Project Completion Status

## Current Progress

### Around 90% Completed

### Core System Completed

* Data collection
* PDF extraction
* Cleaning and filtering
* Knowledge engineering
* Embeddings generation
* Vector database storage
* Retrieval system
* Live stock data integration
* Technical indicators
* LLM integration
* AI trading decision output

### Remaining Professional Upgrades

* Breakout detection
* Pullback detection
* Support/Resistance logic
* Backtesting engine
* Streamlit dashboard UI
* Broker API integration
* Risk engine improvement

---

# Development Phases

---

# Phase 1: Data Collection

## Goal

Collect real trading and finance knowledge.

## What Was Done

Downloaded:

* Zerodha Varsity modules
* Trading books
* Financial PDFs

Stored inside:

```text
/data/pdfs/
```

---

# Phase 2: PDF Extraction

## Goal

Convert PDFs into usable text.

## What Was Done

Created:

```python
extract_all.py
```

Output:

```text
raw_combined.txt
```

Result:

* 13+ PDFs
* 86,000+ raw lines extracted

---

# Phase 3: Cleaning and Filtering

## Goal

Remove useless/noisy PDF content.

## What Was Done

Created:

```python
clean.py
```

Output:

```text
filtered.txt
```

Result:

```text
86,000+ lines → ~4,000 useful lines
```

---

# Phase 4: Knowledge Engineering

## Goal

Convert raw knowledge into structured trading intelligence.

## What Was Done

Created:

```text
knowledge.txt
```

Final Result:

```text
~290 structured lines
```

Categories used:

* [INDICATOR]
* [PATTERN]
* [RISK]
* [LOGIC]
* [CONTEXT]
* [PSYCHOLOGY]

This was the most important phase.

---

# Phase 5: Embeddings

## Goal

Convert knowledge text into vector embeddings.

## What Was Done

Created:

```python
embeddings/store.py
```

Used:

```text
all-MiniLM-L6-v2
```

Result:

Knowledge converted into searchable vectors.

---

# Phase 6: Vector Database

## Goal

Store embeddings permanently.

## What Was Done

Used:

```text
ChromaDB PersistentClient
```

Stored inside:

```text
/db/
```

This became the bot's memory.

---

# Phase 7: Retrieval System

## Goal

Retrieve relevant knowledge for user queries.

## What Was Done

Created:

```python
rag/retrieve.py
```

Example:

```text
What is RSI?
→ returns top relevant knowledge chunks
```

This completed the actual RAG backbone.

---

# Phase 8: Live Stock Data

## Goal

Fetch real market data.

## What Was Done

Created:

```python
data/stock.py
```

Used:

```text
yFinance
```

Example:

```text
TCS.NS → OHLC data
```

---

# Phase 9: Technical Indicators

## Goal

Generate trading signals.

## What Was Done

Created:

```python
indicators/indicators.py
```

Implemented:

* RSI
* EMA
* Trend Detection

---

# Phase 10: LLM Integration

## Goal

Use LLM reasoning for decisions.

## What Was Done

Created:

```python
rag/llm.py
```

Used:

```text
Ollama + Llama 3
```

---

# Phase 11: Final Decision Engine

## Goal

Combine everything.

## What Was Done

Created:

```python
main.py
```

Final Pipeline:

```text
Stock Symbol
→ Yahoo Finance
→ Indicators
→ Retrieval from ChromaDB
→ Llama3 reasoning
→ BUY / SELL / HOLD
```

---

# Practical Learning from This Project

## Technical Learning

### Python Development

* Virtual environments
* Project structure design
* Debugging real-world issues
* File handling
* API usage

### RAG Concepts

* What real RAG means
* Embeddings vs normal text search
* Vector databases
* Retrieval logic
* Persistent memory systems

### AI Engineering

* Prompt engineering
* LLM integration
* Hallucination control
* Decision system design

### Financial Logic

* RSI
* EMA
* Trend detection
* Risk management
* Swing trading logic
* Market psychology

---

# Theoretical Learning

## Key Concepts Learned

### Why Raw PDFs Fail in RAG

Raw PDF text creates weak retrieval.
Cleaning and structured knowledge improve quality significantly.

### Why Prompt Engineering Matters

Even with good data, bad prompts create bad decisions.
Prompt quality directly affects output quality.

### Why HOLD is Important

A strong trading system must know when not to trade.
Sometimes the best trade is no trade.

### Why Strategy Validation Matters

Bad strategy + automation = faster losses.
Decision quality is more important than automation speed.

### Real RAG vs Beginner RAG

Professional systems use:

* retrieval
  n- reranking
* hybrid search
* backtesting
* monitoring

This project built the strong foundation before those upgrades.

---

# Major Challenges Faced

## ChromaDB Persistence Issue

Problem:
Temporary database instead of persistent storage.

Solution:
Used PersistentClient.

---

## yFinance MultiIndex Issue

Problem:
Stock columns returned nested structure.

Solution:
Flattened columns before calculations.

---

## File Reading Issues

Problem:
knowledge.txt loaded empty.

Solution:
Corrected path + encoding.

---

## LLM Wrong Reasoning

Problem:
Incorrect interpretation of RSI.

Solution:
Improved prompt engineering and strict rules.

---

# Future Improvements

## Professional Upgrades Planned

* Backtesting engine
* Breakout detection
* Pullback detection
* Support/Resistance detection
* Streamlit dashboard
* Broker API integration
* Portfolio tracking
* Live alerts
* Trade execution automation

---

# Final Result

This project is not a basic chatbot.

It is an:

## AI-Powered Financial Decision System

that uses:

* knowledge
* retrieval
* market data
* technical indicators
* LLM reasoning

for intelligent trading decisions.

This project is portfolio-worthy, hackathon-worthy, and strong for internships in AI, FinTech, and Quant development.
