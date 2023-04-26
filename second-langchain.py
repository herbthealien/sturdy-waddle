from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
proompty = PromptTemplate(
    input_variables=["moovie"],
    template="What is a good name for a movie about {moovie}?"
)
print("What's the subject of your movie? Let me know and I'll name it for you.")

print(llm(proompty.format(moovie=input())))