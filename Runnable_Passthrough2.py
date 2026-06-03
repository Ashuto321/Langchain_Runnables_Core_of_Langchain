from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = "write a joke on the topic {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "explain the joke {joke}",
    input_variables = ["joke"]
)

model = ChatGroq(model = "openai/gpt-oss-120b", temperature=0.7)

parser = StrOutputParser()

# chian 1
joke_chain = RunnableSequence(prompt1, model, parser)

# chain 2
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

# combined the chains 1 and 2

final_chain = RunnableSequence(joke_chain, parallel_chain)

response = final_chain.invoke({"topic": "programming"})

print(response)