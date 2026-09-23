import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY and "GOOGLE_API_KEY" in st.secrets:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
genai.configure(api_key=GOOGLE_API_KEY)

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = get_embeddings()
    vector_store = FAISS.from_texts(
        text_chunks,
        embedding=embeddings
    )
    return vector_store


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3
    )

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question):
    vector_store = st.session_state.get("vector_store")

    if vector_store is None:
        st.warning("Please upload and process PDF files first.")
        return

    docs = vector_store.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain.invoke(
        {
            "input_documents": docs,
            "question": user_question
        }
    )

    st.write("Reply: ", response["output_text"])



def main():
    st.set_page_config(
        page_title="PDF Insight AI",
        page_icon="📚"
    )

    st.header("PDF Insight AI 📚 — Chat Agent 🤖")

    user_question = st.text_input("Ask a Question from the PDF Files uploaded .. ✍️📝")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        
        st.title("📁 PDF Files")
        st.write("Upload your PDF files and click on the Submit & Process Button.")
        pdf_docs = st.file_uploader(
            "Upload your PDF files",
            accept_multiple_files=True
    )
        if st.button("Submit & Process"):
            with st.spinner("Processing..."): # user friendly message.
                raw_text = get_pdf_text(pdf_docs) # get the pdf text
                text_chunks = get_text_chunks(raw_text) # get the text chunks
                vector_store = get_vector_store(text_chunks) # create vector store
                st.session_state["vector_store"] = vector_store
                st.success("Done")
        
        st.write("---")
        st.image("img/my_logo.png", width=150)
        st.write("Built by Sumayya")


    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: #0E1117; padding: 15px; text-align: center;">
            PDF Insight AI | Built by Sumayya
        </div>
        """,
        unsafe_allow_html=True
    )
if __name__ == "__main__":
    main()