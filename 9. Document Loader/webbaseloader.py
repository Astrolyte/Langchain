from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.flipkart.com/apple-macbook-neo-a18-pro-2026-pro-8-gb-256-gb-ssd-tahoe-mhfh4hn-a/p/itmca8bd5b2e2477?pid=COMHZQX4DAXF5U9M&lid=LSTCOMHZQX4DAXF5U9MJGYTMC&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=599aa25e-7b4d-4fdb-aebb-34665bd600b4.COMHZQX4DAXF5U9M.SEARCH&ppt=None&ppn=None&ssid=2smegzd3tc0000001786379560109&ov_redirect=true'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)