from sentence_transformers import SentenceTransformer
import chromadb
import os

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Base path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Same DB path
DB_PATH = os.path.join(BASE_DIR, "db")

# SAME persistent client
client = chromadb.PersistentClient(path=DB_PATH)

# SAME collection
collection = client.get_or_create_collection(
    name="trading_knowledge"
)


def retrieve(query, n=5):
    if not query.strip():
        return []

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n
    )

    docs = results.get("documents", [])

    if not docs or len(docs[0]) == 0:
        return []

    return docs[0]


if __name__ == "__main__":
    query = input("Enter query: ")

    results = retrieve(query)

    print("\nTop Results:\n")

    if not results:
        print("❌ No results found.")
    else:
        for item in results:
            print("-", item)