from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
)

print("Choose your Agent wisely!!!")
print("Enter 1 for Angry Agent")
print("Enter 2 for Sad Agent")
print("Enter 3 for Funny Agent")

choice = input("Type your response: ")

if choice == "1":
  mode = "You are an Angry AI agent. You respond aggressively and impatiently."
elif choice == "2":
  mode = "You are a very sad AI agent. You respond in a depressed and emotional tone"
elif choice == '3':
  mode = "You are a very Funny AI agent. You respond with humor and jokes."

messages= [
  SystemMessage(content=mode)
]

while True:
  print("---------------\nWelcome !!!!!\nType 0 to exit the Application\n---------------")
  prompt = input("You: ")
  messages.append(HumanMessage(content=prompt))
  if prompt == "0":
    break
  response = model.invoke(messages)
  messages.append(AIMessage(content=response.text))
  print("Bot: ", response.text)

print(messages)