from flask import Flask, request, jsonify
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from utils.db_helpers import get_db_connection
import psycopg2

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="novacept",
    user="postgres",
    password="nishika@1234"
)

# Load Chroma vector database
chroma_client = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())

# Initialize conversational chain
chat_chain = ConversationalRetrievalChain.from_llm(
    llm_name="gpt-3.5 turbo", 
    retriever=chroma_client.as_retriever()
)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    question = data.get('question')
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({"error": "User must be authenticated"}), 401

    with conn.cursor() as cursor:
        cursor.execute("SELECT preferences FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()

    response = chat_chain.run(input=question)
    return jsonify({"response": response})

@app.route('/add-data', methods=['POST'])
def add_data():
    data = request.json
    documents = data.get("documents")
    
    for doc in documents:
        chroma_client.add_texts([doc['text']], metadatas={"source": doc['source']})
    
    return jsonify({"status": "Data added successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




# WhatsApp Integration Approach:
# 1. Use the Twilio API for WhatsApp or Meta's WhatsApp Business API to send and receive messages.
# 2. Set up a webhook to handle incoming WhatsApp messages:
#    - Twilio provides a public URL to configure a webhook.
#    - Meta's WhatsApp Business API requires you to set up a webhook endpoint in Flask (e.g., /webhook/whatsapp).
# 3. Incoming messages will be received at the webhook, which you need to parse and send to your LangChain backend for processing.
# 4. Use the `twilio` Python library or HTTP requests to send responses back to WhatsApp users.