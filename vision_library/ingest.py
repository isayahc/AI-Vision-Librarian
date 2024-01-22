import os

from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings import ClarifaiEmbedding

# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

CLARIFAI_PAT = os.getenv("CLARIFAI_PAT")


embed_model = ClarifaiEmbedding(
    model_name="BAAI-bge-base-en", 
    user_id="clarifai", 
    app_id="main",
    pat=CLARIFAI_PAT,
)



documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist()