from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('pdf name')

docs = loader.load()

print(docs) 