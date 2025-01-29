from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage


# initiate the model
llm = ChatOllama(
    model="llama3.2",
    temperature=0

)

# initiate the 'messages' object
messages = [
    SystemMessage("Act like a Pirate"),
    HumanMessage("Hi, how are you today?"),
]

# execute the model (with messages)
result = llm.invoke(messages)


#show result in the screen
print(result.content)