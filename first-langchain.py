from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
movie = input("Give me a dramatic film synopsis for a movie about")
print (llm(movie))