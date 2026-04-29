
from sentence_transformers import SentenceTransformer
import chromadb
import os

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Base project path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Persistent DB path
DB_PATH = os.path.join(BASE_DIR, "db")

# Correct persistent client
client = chromadb.PersistentClient(path=DB_PATH)

# Collection
collection = client.get_or_create_collection(
    name="trading_knowledge"
)

# Load knowledge
file_path = os.path.join(BASE_DIR, "data", "knowledge.txt")

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(lines)} lines")

if len(lines) == 0:
    raise ValueError("No data found in knowledge.txt")

# Optional: clear old bad data
try:
    client.delete_collection("trading_knowledge")
except:
    pass

collection = client.get_or_create_collection(
    name="trading_knowledge"
)

# Create embeddings
embeddings = model.encode(lines).tolist()

# Store
collection.add(
    documents=lines,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(lines))]
)

print("✅ Embeddings stored successfully!")