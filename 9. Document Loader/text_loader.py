from langchain_community.document_loaders import TextLoader
loader = TextLoader("path",encoding = 'utf-8')

docs = loader.load()

