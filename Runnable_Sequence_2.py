from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1= PromptTemplate(
    template = "write a joke on the topic {topic}",
    input_variables = ["topic"]
)

model = ChatGroq(model = "openai/gpt-oss-120b", temperature=0.7)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = "explain the joke {joke}",
    input_variables =["joke"]
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

response = chain.invoke({"topic": "programming"})

print(response)