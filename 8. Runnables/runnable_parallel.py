from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation"
)
model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template = 'Generate a twwet post about {topic}',
    input_variable = ['topic']
)
prompt2 = PromptTemplate(
    template = 'Generate a linkedin post about {topic}',
    input_variable = ['topic']
)
parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'linkedin':RunnableSequence(prompt2,model, parser)
})
result = parallel_chain.invoke({'topic':'AI'})

print(result)