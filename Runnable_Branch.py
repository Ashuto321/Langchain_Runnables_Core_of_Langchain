from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile", temperature=0.7)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template ="generate a 4 line report on topic {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template ="generate a 4 point summary on topic {topic}",
    input_variables = ["topic"]
)

# chain 1
report_chain = RunnableSequence(prompt1, model, parser)

# chain 2
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>50, RunnableSequence(prompt2, model, parser)),
    # default case
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_chain, branch_chain)

response = final_chain.invoke({"topic": "AI"})

print(response)

final_chain.get_graph().print_ascii()