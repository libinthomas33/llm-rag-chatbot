from datetime import datetime

from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

company_policy_path = "data"
OPENAI_API_KEY = "sk-YOUR_OPENAI_API_KEY"

# Load and split documents
raw_documents = DirectoryLoader(company_policy_path).load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)

# Set up the vector database
db = Chroma.from_documents(
    documents,
    OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY),
    persist_directory="chroma_db",
)

# Configure the language model
llm = ChatOpenAI(model="gpt-4-turbo", openai_api_key=OPENAI_API_KEY)

# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are AI Agent who can help the employees with questions about company policies and procedures. 
            Traditionally, they might need to search through a company intranet, HR portal, or email HR directly. 
            This process can be time-consuming and inefficient, especially for simple questions. 
            Use this context to answer the questions `{company_policy_info}`. Today is `{current_date}`""",
        ),
        (
            "human",
            "{question}",
        ),
    ]
)

# Create the language model chain with the prompt template
chain = prompt | llm 

print("\nHello, how are you? I'm XYZ bot.\n")

while True:
    current_date = datetime.now()
    user_input = input("I'm here to assist you. Ask me something. To exit, type 'q': ")

    if user_input.lower() == "q":
        print("\nExiting. Have a great day!\n")
        break

    # Perform a similarity search in the vector database
    docs = db.similarity_search(user_input)
    
    # Generate a response using the language model
    resp = chain.invoke(
        {
            "question": user_input,
            "company_policy_info": docs[0].page_content,
            "current_date": current_date,
        }
    )
    
    print("\nXYZ bot: ", resp.content)
    print("\n______________________________________________________\n")
