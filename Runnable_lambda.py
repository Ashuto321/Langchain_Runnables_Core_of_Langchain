from langchain_core.runnables import RunnableLambda


def word_count(text):
    return len(text.split())

word_count_runnable = RunnableLambda(word_count)

response = word_count_runnable.invoke("hello how are you doing today")

print(response)