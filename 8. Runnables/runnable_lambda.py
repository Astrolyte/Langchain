from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableSequence, RunnableLambda
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

def word_count(text):
    return len(text.split())

joke_gen = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})
final_chain = RunnableSequence(joke_gen,parallel_chain)

print(final_chain.invoke({'topic':'AI'}))

