from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = "generate a short joke on the topic {topic}",
    input_variables = ["topic"]
)

# for wordcount we have a function
def word_count(text):
    return len(text.split())

model = ChatGroq(model = "llama-3.3-70b-versatile", temperature=0.7)

parser = StrOutputParser()

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)

response = final_chain.invoke({"topic": "programming"})

print(response)

final_chain.get_graph().print_ascii()
