from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

passthrough = RunnablePassthrough()
result = passthrough.invoke({"input": "hello ashutosh "})

# it will return the input as it is without any changes
print(result)