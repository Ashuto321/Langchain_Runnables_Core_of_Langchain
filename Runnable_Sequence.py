from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template = "write a joke on the topic {topic}",
    input_variables = ["topic"]
)

model = ChatGroq(model = "openai/gpt-oss-120b", temperature=0.7)

parser = StrOutputParser()

# now we have all the components we can craete a runnablesequence
chain = RunnableSequence(prompt, model, parser)

# now we can call the chain with the input variables for the prompt
response = chain.invoke({"topic": "programming"})
print(response)