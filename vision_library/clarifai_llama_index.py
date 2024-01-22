from llama_index.llms import ChatMessage, MessageRole
from llama_index.prompts import ChatPromptTemplate

from llama_index.embeddings import ClarifaiEmbedding
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import LiteLLM
from llama_index.llms import Clarifai
from llama_index.llms import OpenAI
import os
import dotenv
from llama_index import StorageContext, load_index_from_storage

CLARIFAI_PAT = os.getenv("CLARIFAI_PAT")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# embed_model = ClarifaiEmbedding(
#     model_name="BAAI-bge-base-en", 
#     user_id="clarifai", 
#     app_id="main",
#     pat=CLARIFAI_PAT,
# )

llm = OpenAI()


# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)

# Create a ServiceContext
# service_context = ServiceContext.from_defaults(
#     llm=llm, embed_model=embed_model
# )

# Load your documents
documents = SimpleDirectoryReader('data').load_data()

# Build the index
# index = VectorStoreIndex.from_documents(
#     documents=documents, service_context=service_context
# )

# query_engine = index.as_query_engine()
# response = query_engine.query("Looking for a person of african descendant")
# print(response)

# Text QA Prompt
chat_text_qa_msgs = [
    ChatMessage(
        role=MessageRole.SYSTEM,
        content=(
            "There is a directory full of .txt files of  the format of the image url in\
            first line and the list of tags in the rest of the lines\
            are tags that describe the image. The user will ask for images and you must provide them the url of the images you have picked\
            as well as well as why you picked those images"
        ),
    ),
    ChatMessage(
        role=MessageRole.USER,
        content=(
            "Context information is below.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Given the context information and not prior knowledge, "
            "answer the question: {query_str}\n"
        ),
    ),
]
text_qa_template = ChatPromptTemplate(chat_text_qa_msgs)

# Refine Prompt
chat_refine_msgs = [
    ChatMessage(
        role=MessageRole.SYSTEM,
        content=(
            "Always answer the question, even if the context isn't helpful."
        ),
    ),
    ChatMessage(
        role=MessageRole.USER,
        content=(
            "We have the opportunity to refine the original answer "
            "(only if needed) with some more context below.\n"
            "------------\n"
            "{context_msg}\n"
            "------------\n"
            "Given the new context, refine the original answer to better "
            "answer the question: {query_str}. "
            "If the context isn't useful, output the original answer again.\n"
            "Original Answer: {existing_answer}"
        ),
    ),
]
refine_template = ChatPromptTemplate(chat_refine_msgs)

# Now, use the prompts in your query
query_engine = index.as_query_engine(
    text_qa_template=text_qa_template, 
    refine_template=refine_template
)
# response = query_engine.query("Looking for a person of african descendant")

# print(response)
# response = query_engine.query("Looking for a image related to music or art")
# response = query_engine.query("Looking for images with women in them")
# response = query_engine.query("Looking fun images make sure to provide the image url ")
# response = query_engine.query("Looking images for my sports blog. Do not mention the tags. Provide the image urls. These documents have urls at the tops followed by a list of tags torepresent the image")
# print(response)
# x=0