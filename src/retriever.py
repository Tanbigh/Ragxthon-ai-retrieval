from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from embeddings import load_embedding_model

def create_vector_store():

    loader = TextLoader("data/dataset.txt")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    texts = text_splitter.split_documents(documents)

    embeddings = load_embedding_model()

    vectorstore = FAISS.from_documents(texts, embeddings)

    return vectorstore