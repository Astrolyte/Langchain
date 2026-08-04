from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation"
)

model1 = ChatHuggingFace(llm = llm)

llm2 = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    task = "text-generation"
)
model2 = ChatHuggingFace(llm = llm2)

prompt1 = PromptTemplate(
    template = "generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template = "generate 5 question and asnwers from the following text \n {text}",
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template = "merge the provided notes and quiz into a single document \n notes -> {notes} and quiz-> {quiz}",
    input_variables=['notes','quiz']
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser 

chain = parallel_chain | merge_chain

text = """ Notes:

For the Code Agent tasks among the public benchmarks above, DeepSeek-V4-Flash-0731 is evaluated with the minimal mode of DeepSeek Harness (to be released) as the agent framework, using the max reasoning effort level with temperature = 1.0, top_p = 0.95.
† DSBench-FullStack is an internal full-stack development test set; DSBench-Hard is an internal test set of difficult coding-agent problems.
Chat Template
This release does not include a Jinja-format chat template. Instead, we provide a dedicated encoding folder with Python scripts and test cases demonstrating how to encode messages in OpenAI-compatible format into input strings for the model, and how to parse the model's text output. Please refer to the encoding folder for full documentation.

The reasoning_effort parameter now supports three levels — low, high, and max — which control how much deliberation the model spends before answering."""

# result = chain.invoke({'text':text})

# print(result)

chain.get_graph().print_ascii()