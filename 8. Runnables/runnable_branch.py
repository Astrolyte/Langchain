from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableSequence, RunnableLambda, RunnableBranch
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template = "Summarize the following text \n{text}",
    input_variables=['text']
)

llm = HuggingFaceEndpoint(
    repo_id= "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation"
)

parser = StrOutputParser()

model = ChatHuggingFace(llm = llm)

report_gen_chain = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))