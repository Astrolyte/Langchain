from langchain_community.tools import DuckDuckGoSearchRun
searchtool = DuckDuckGoSearchRun()

results = searchtool.invoke("ipl news")

print(results)