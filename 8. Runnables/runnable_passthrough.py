from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableSequence
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

passthrough = RunnablePassthrough()

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
parser = StrOutputParser()

model = ChatHuggingFace(llm = llm)

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation': RunnableSequence(prompt2,model , parser)
    }
)
final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({'topic':'cricket'})
print(result)
