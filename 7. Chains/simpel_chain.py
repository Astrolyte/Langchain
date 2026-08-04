from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt = PromptTemplate(
    template = "generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

llm = HuggingFaceEndpoint(
    repo_id= "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation"
)
model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()