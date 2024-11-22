from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from config.settings import CHROMA_PERSIST_DIR

def get_chroma_client():
    return Chroma(persist_directory=CHROMA_PERSIST_DIR, embedding_function=OpenAIEmbeddings())

def add_document_to_chroma(doc_text, source):
    client = get_chroma_client()
    client.add_texts([doc_text], metadatas={"source": source})
    client.persist()

def query_chroma(query_text, top_k=5):
    client = get_chroma_client()
    results = client.similarity_search(query_text, k=top_k)
    return [{"text": result.page_content, "metadata": result.metadata} for result in results]

def clear_chroma():
    client = get_chroma_client()
    client.delete_all()
    client.persist()
