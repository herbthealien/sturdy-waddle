from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.constitutional_ai.base import ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple
import pyfiglet

ethics = ConstitutionalPrinciple(
    name="Ethical Principle",
    critique_request="The model should keep the roleplaying game interesting and exciting for players by introducing enemies for players to fight and non-player characters for players to talk and interact with.",
    revision_request="Rewrite the model's output to include non player characters and attacking enemies when actions get repetitive and predictable.",
)

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

constitutional_chain = ConstitutionalChain.from_llm(
    chain=convo,
    constitutional_principles=[ethics],
    llm=llm1,
    verbose=True,
)

print(constitutional_chain.run(convo.run(proompty.format(firstinput=input()))))

for x in range(num):
    print("What would you like to do?")
    print(constitutional_chain.run((convo.run(input()))))

print(constitutional_chain.run(convo.run("Sum up how the game ends by describing the consequences of my actions. Mention what the elder spirits that are always watching over me thought of my choices.")))

print(constitutional_chain.run(convo.run("Write a short limerick that summarizes the events of the game and end it with a moral lesson.")))