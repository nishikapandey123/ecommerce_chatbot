import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

# Load the OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if not openai_api_key:
    raise ValueError("OpenAI API key is not set. Please set the 'OPENAI_API_KEY' environment variable.")

# Initialize Chroma DB with OpenAI embeddings
chroma_client = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings(openai_api_key=openai_api_key))

# Example: Adding product manuals and customer tickets
documents = [
    {"text": "How to assemble product X.", "source": "manual"},
    {"text": "Battery not charging issue.", "source": "ticket"}
]

for doc in documents:
    chroma_client.add_texts([doc["text"]], metadatas={"source": doc["source"]})

chroma_client.persist()
