# data/clean.py

input_file = "data/raw_combined.txt"
output_file = "data/filtered.txt"

keywords = [
    "RSI", "EMA", "MACD", "trend", "support", "resistance",
    "breakout", "pullback", "volume", "momentum",
    "stop loss", "risk", "reward", "buy", "sell"
]

filtered_lines = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        
        if len(line) < 30:
            continue
        
        for keyword in keywords:
            if keyword.lower() in line.lower():
                filtered_lines.append(line)
                break

with open(output_file, "w", encoding="utf-8") as f:
    for line in filtered_lines:
        f.write(line + "\n")

print(f"Filtered {len(filtered_lines)} lines.")