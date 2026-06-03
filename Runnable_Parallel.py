from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1= PromptTemplate(
    template = "write a tweet in 2 lines on the topic {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "write a LinkedIn in 2 lines post on the topic {topic}",
    input_variables =["topic"]
)

model = ChatGroq(model = "openai/gpt-oss-120b", temperature=0.7)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet" : RunnableSequence(prompt1, model, parser),
    "linkedin" : RunnableSequence(prompt2, model, parser)
})

parallel_response = parallel_chain.invoke({"topic":"AI"})

print(parallel_response)
# also you can do

print("tweet", parallel_response["tweet"])
print("Linkedin", parallel_response["linkedin"])