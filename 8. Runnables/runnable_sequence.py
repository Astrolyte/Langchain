from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables=['topic']
)

llm = HuggingFaceEndpoint(
    repo_id= "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation"
)
prompt2 = PromptTemplate(
    template = "Explain the joke {joke}",
    input_variables=["joke"]
)
model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

chain = RunnableSequence(prompt , model , parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))