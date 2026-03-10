import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def load_documents(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        docs = [line.strip() for line in f.readlines() if line.strip()]
    return docs


def load_queries(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        queries = [line.strip() for line in f.readlines() if line.strip()]
    return queries


def retrieve_most_relevant(query: str, documents: list, model) -> tuple:
    doc_embeddings = model.encode(documents)
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    best_index = np.argmax(similarities)
    best_doc = documents[best_index]

    return best_doc, similarities[best_index]


def main():

    model = SentenceTransformer("all-MiniLM-L6-v2")

    documents = load_documents("documents.txt")
    queries = load_queries("queries.txt")

    results = []

    for query in queries:
        doc, score = retrieve_most_relevant(query, documents, model)

        output = f"Query: {query}\nRetrieved Document:\n{doc}\nSimilarity Score: {score:.4f}\n\n---\n"
        print(output)
        results.append(output)

    with open("results.txt", "w", encoding="utf-8") as f:
        f.writelines(results)


if __name__ == "__main__":
    main()