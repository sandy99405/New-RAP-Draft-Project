# import warnings
# warnings.filterwarnings("ignore", category=UserWarning)

import os
from pathlib import Path
from dotenv import load_dotenv

script_dir = Path(__file__).resolve().parent
env_path = script_dir / ".env"

load_dotenv()

#load_dotenv(dotenv_path=env_path)

print("OPENAI_API_KEY found:", bool(os.getenv("OPENAI_API_KEY")))


from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

#model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
model = init_chat_model("openai:gpt-4o")
print("Hello world")
response = model.invoke("What is LangChain in one sentence?")
print("=== Model Response ===")
print(response.content)
print()

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.chat_history import InMemoryChatMessageHistory
# from langchain_core.messages import HumanMessage, AIMessage

# memory = InMemoryChatMessageHistory()

# memory.add_message(HumanMessage(content="My name is Sandilya and I love Inchara"))
# memory.add_message(AIMessage(content="Nice to meet you, Sandilya!!, Inchara love you too"))
# memory.add_message(HumanMessage(content="What tools should I learn first?"))
# memory.add_message(AIMessage(content="Start with PromptTemplates and simple chains, then move to tools and agents"))
# memory.add_message(HumanMessage(content="Yesterday Sandilya and Inchara had lunch date"))
# memory.add_message(AIMessage(content="That's great! Hope you both had a wonderful time together."))
# print("=== Memory Content ===")
# for msg in memory.messages:
#     print(f"  [{msg.type}: {msg.content[:80]}...")
# print()


# chat_with_memory = ChatPromptTemplate.from_messages([
#     ("system", "{instruction}"),
#     ("placeholder", "{history}"),
#     ("human", "{question}"),
#     ("human", "{question1}"),
#     ("human", "{question2}"),
#     ("human", "{question3}"),   
#     ("human", "{question4}"),
#     ("human", "{question5}"),
# ])

# chain_with_memory = chat_with_memory | model | StrOutputParser()

# result = chain_with_memory.invoke({
#     "instruction": "You are a helpful assistant that answers questions based on the conversation history.",
#     "history": memory.messages,
#     "question": "What was my name again?",
#     "question1": "Whom does Inchara Love?",
#     "question2": "Can you ask me a question about my name and Inchara?",
#     "question3": "What did Sandilya and Inchara do yesterday?",
#     "question4": "What is the relationship between Sandilya and Inchara?",
#     "question5": "Does Inchara have a boyfriend?",
# })

# print("=== Memory-Aware Response ===")
# print(result)
# print()




from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser


memory = InMemoryChatMessageHistory()

memory.add_message(AIMessage(content="Hi my name is friday"))
memory.add_message(HumanMessage(content="Hi Friday, my name is Sandilya. I am SAP Developer aspirant and preparing to enter in SAP Company within 3-4 months"))
memory.add_message(AIMessage(content="Wow that's great Sandilya, how can I help you?"))

for m in memory.messages:
    print(f"  [{m.type}: {m.content[:80]}...")
print()


chat_template = ChatPromptTemplate.from_messages([
        ("system","{instruction}"),
        ("placeholder","{history}"),
        ("human", "{question}"),  
])


chain_model = chat_template | model | StrOutputParser()


result = chain_model.invoke({
         "instruction": "You are a Training Model that helps Sandilya to get into SAP Company",
         "history": memory.messages,
         "question": "What can I do to get into SAP Company?",   
})

print(result)












# from langchain.chat_models import init_chat_model

# model = init_chat_model("chatgpt:5.5")

# result = model.invoke("Explain about LangChain")

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# prompt = ChatPromptTemplate.format_prompt("Explain {template}")

# chain = prompt | model | StrOutputParser()

# result = chain.invoke({"template":"LangChain"})




# from langchain_mcp_adapters.client import MultiServerMCPClient
# from langchain.agents import create_agent

# async def main():
#     """
#     Main async function - MCP connections are async because the involve I/O (spawning processes, netwrok calls).
#     """

#     current_dir = os.path.dirname(os.path.abspath(__file__)) 
#     server_path = os.path.join(current_dir,"mcp_math_server.py")   

#     client = MultiServerMCPClient(
#     {
#         "math": {
#             "command":"python",
#             "args": [server_path],
#             "transport": "stdio",       
#         },

#     }
#     ) 

#     tools = await client.get_tools()

#     print("=" * 55)
#     print("MCP Agent - Tools discovered from MCP Server")
#     print("=" * 55)
#     print(f"\n Found {len(tools)} tools from MCP server:\n")
#     for t in tools:
#         print(f" {t.name}: {t.description[:60]}")
#     print()    


# #Create the agent
#     agent = create_agent(
#         model,
#         tools=tools,
#     )

# # Run the agent

#     async def run_agent(question:str):
#         """Run the agent and print the execution trace."""
#         print(f"User: {question}")
#         print("-" *50)

#         result = await agent.ainvoke({
#             "messages": [("user",question)]
#         })

#         for msg in result["messages"]:
#             if msg.type == "human":
#                 continue
#             elif msg.type == "ai":
#                 if msg.tools_calls:
#                     for tc in msg.tool_calls:
#                         print(f" Agent thinks -> calling: {tc['name']}({tc['args']})")
#                 elif msg.content:
#                     print(f"Agent answer: {msg.content}")
#             elif msg.type == 'tool':
#                 content = msg.content

#                 if isinstance(content, list):
#                     texts = [item["text"] for item in content if isinstance(item, dict) and "text" in item] 
#                     content = ",".join(texts) if texts else str(content)
#                 print(f"Tool result: {content}")
#         print("="*55)
#         print()

#     await run_agent("What is Inchara + Sandilya?")

#     print("MCP Agent demo complete")



