from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import pyfiglet

llm1 = OpenAI(temperature=0.9)

welcome = pyfiglet.figlet_format("AI RPG")

print(welcome)

print("Play a short roleplaying game with artificial intellince as your Dungeon Master!")

print("Please specify the number of turns you'd like to take:")

num = int(input())

print("You are in a dark room that smells of frankincense. What would you like to do?")

proompty = PromptTemplate(
    input_variables=["firstinput"],
    template="We are playing a roleplaying game together. You are leading the game, you decide what happens when I take actions in the game. The game has started, and I'm in a dark room that smells of frankincense. I would like to {firstinput}. What happens when I do this?"
)

#commenting this old code out in case I need it later print(llm1(proompty.format(firstinput=input())))

convo = ConversationChain(
    llm=OpenAI(temperature=0),
    memory=ConversationBufferMemory()
)

print(convo.run(proompty.format(firstinput=input())))

for x in range(num):
    print("What would you like to do?")
    print(convo.run(input()))

print(convo.run("Sum up how the game ends by describing the consequences of my actions. Mention what the elder spirits that are always watching over me thought of my choices."))

print(convo.run("Write a short limerick that summarizes the events of the game and end it with a moral lesson."))