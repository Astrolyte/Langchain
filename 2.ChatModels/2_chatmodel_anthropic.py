from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = "claude-3-5")

result = model.invoke("what is the capital of india")

print(result.content)