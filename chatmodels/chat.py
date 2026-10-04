from dotenv import load_dotenv

load_dotenv()

# from langchain.chat_models import init_chat_model
from langchain_deepseek import ChatDeepSeek

# model = init_chat_model("gpt-4.1")

# response = model.invoke("Why do parrots talk?")

# print(response.content)
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

ai_msg = llm.invoke("Write a poem on AI")
print(ai_msg.content)