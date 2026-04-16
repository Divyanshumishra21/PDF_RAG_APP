import streamlit as st
import os

from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.chain import get_rag_chain

st.set_page_config(page_title="PDF RAG App",layout="wide")

st.title("📄 PDF Question Answering System")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    # Step 1: Load
    documents = load_pdf(file_path)

    # Step 2: Split
    chunks = split_documents(documents)

    # Step 3: Embeddings
    embeddings = get_embeddings()

    # Step 4: Vector DB
    vectorstore = create_vector_store(chunks, embeddings)

    # Step 5: Retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # Step 6: RAG Chain
    rag_chain = get_rag_chain(retriever)

    # Query Input
    query = st.text_input("Ask a question from the PDF")

    if query:
        with st.spinner("Generating answer..."):
            answer = rag_chain.invoke(query)

        st.write("### Answer:")
        st.write(answer)