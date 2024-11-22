**Ecommerce Chatbot**

**Project Overview**

This project is an **AI-powered Ecommerce Chatbot** designed to reduce customer support workload by providing automated responses to customer queries. It retrieves information from product manuals, customer tickets, and other data sources to offer efficient and accurate assistance.

The chatbot is built to work on multiple platforms such as **websites** and **WhatsApp**, and it integrates a conversational retrieval system for dynamic query handling.

---

## **Features**

- **Conversational Retrieval**: Uses **LangChain** to process and respond to user queries dynamically.
- **Multi-Modal Data Access**: Handles product manuals (including images), customer tickets, and other relevant data.
- **Multi-Channel Support**: Designed for deployment on websites and WhatsApp.
- **Secure User Authentication**: Ensures only authenticated users can interact with the chatbot or raise support tickets.
- **Containerized Application**: Dockerized for portability and ease of deployment.
- **Customizable**: Easily extendable to include new data sources and additional integration platforms.

---

## **Technologies Used**

1. **Backend**:
   - **Flask**: Handles API endpoints for user interactions and data processing.
   - **LangChain**: Manages conversational logic and retrieval-augmented generation (RAG) pipelines.
   - **Chroma**: Used as a vector database to store and retrieve embeddings.

2. **Frontend**:
   - **Streamlit**: Provides a simple web-based interface for testing the chatbot.

3. **Database**:
   - **PostgreSQL**: Stores structured user data like authentication details and preferences.

4. **Containerization**:
   - **Docker**: Ensures the application is portable and scalable.

5. **Environment Management**:
   - **Python-dotenv**: Manages sensitive environment variables like API keys.

6. **Authentication**:
   - Basic user ID validation from PostgreSQL database.
   - Extendable to token-based authentication (e.g., JWT).

---

## **How It Works**

1. **Data Initialization**:
   - **`init_chroma.py`** initializes the Chroma vector database with product manuals and customer tickets. Embeddings are generated using **OpenAI embeddings** and stored for efficient retrieval.

2. **Database Setup**:
   - **`init_db.py`** creates the necessary PostgreSQL tables for storing user preferences and data sources.

3. **Backend API**:
   - **`app.py`** provides REST API endpoints:
     - `/query`: Accepts user questions, processes them through LangChain’s conversational retrieval chain, and returns responses.
     - `/add-data`: Adds new documents (e.g., product manuals) to the Chroma vector database.

4. **Frontend Interaction**:
   - The **Streamlit app** provides a user-friendly interface to interact with the chatbot. Users can input queries and view responses directly in the app.

5. **Authentication**:
   - User authentication is implemented by validating `user_id` against the PostgreSQL database. This ensures secure interaction.

6. **Multi-Channel Design**:
   - The chatbot is designed to integrate with platforms like websites and WhatsApp. Integration strategies are outlined for using APIs like **Twilio** for WhatsApp.

---

## **Setup and Deployment**

### **1. Clone the Repository**
```bash
git clone https://github.com/nishikapandey123/ecommerce_chatbot.git
cd ecommerce_chatbot
```

### **2. Install Dependencies**
Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Set Up Environment Variables**
Create a `.env` file in the root directory with the following content:
```plaintext
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=your_postgresql_url
```

### **4. Initialize Database**
Run the following command to set up the PostgreSQL database:
```bash
python init_db.py
```

### **5. Initialize Chroma Database**
Add product manuals and tickets to the vector store:
```bash
python init_chroma.py
```

### **6. Run the Application**
Start the Flask backend:
```bash
python app.py
```
Run the Streamlit frontend:
```bash
streamlit run streamlit_app.py
```

---

## **Future Enhancements**

- **Advanced Authentication**: Implement JWT for more secure user authentication.
- **Additional Platforms**: Integrate with WhatsApp, Facebook Messenger, and other channels using APIs like Twilio and Meta’s Graph API.
- **Advanced Data Sources**: Add more dynamic data sources like video-based troubleshooting from the intranet.
- **Scalability**: Use Kubernetes or Docker Swarm for load balancing and scaling.

---

## **Contact**

For queries, please contact [nishikapandey123](mail to :nishikapandey2000@gmail.com).
