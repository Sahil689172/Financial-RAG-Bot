from data.stock import get_stock_data
from indicators.indicators import compute_ema, compute_rsi, detect_trend
from rag.retrieve import retrieve
from rag.llm import ask_llm

print("=== FINANCIAL RAG BOT ===\n")

symbol = input("Enter stock symbol (example: TCS.NS): ")

# Fetch stock data
df = get_stock_data(symbol)

# Indicators
df = compute_ema(df)
df = compute_rsi(df)

latest_rsi = round(df["RSI"].iloc[-1], 2)
trend = detect_trend(df)

# Retrieval query
query = f"RSI is {latest_rsi} and trend is {trend}"

knowledge = retrieve(query, n=5)

retrieved_text = "\n".join(knowledge)

# Final Prompt
prompt = f"""
You are a professional swing trading assistant.

Analyze the stock using technical analysis and retrieved financial knowledge.

----------------------------------
STOCK DATA

Stock: {symbol}
RSI: {latest_rsi}
Trend: {trend}

----------------------------------
RETRIEVED KNOWLEDGE

{retrieved_text}

----------------------------------

STRICT ANALYSIS RULES:

1. RSI < 30 = Oversold
2. RSI > 70 = Overbought
3. RSI 40–60 = Neutral zone
4. In DOWNTREND, avoid aggressive BUY decisions
5. If signals conflict → prefer HOLD
6. Never invent facts not supported by data
7. Risk management is mandatory

----------------------------------

Return ONLY in this exact format:

Decision: BUY / SELL / HOLD

Confidence: LOW / MEDIUM / HIGH

Reason:
- point 1
- point 2
- point 3

Risk:
- main risk factor
"""

result = ask_llm(prompt)

print("\n========== AI DECISION ==========\n")
print(result)