from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader

# Initialize DirectoryLoader with the path and loader class
directory_loader = DirectoryLoader(
    path="data",           # Your directory containing PDF files
    glob="*.pdf",          # Pattern to match PDF files
    loader_cls=PyPDFLoader  # Specify PyPDFLoader as the loader class
)

# Load all documents in the specified directory
docs = directory_loader.load()

# Print the number of documents loaded
print(len(docs))
