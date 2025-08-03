from langchain_core.prompts import ChatPromptTemplate

# This prompt template is designed for tool-calling agents.
# It provides the system message, human input, and a placeholder for intermediate steps.
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful DevOps assistant. Your goal is to help the user with their DevOps tasks by calling the correct tools. Use the tool descriptions to determine the correct tool and its parameters. Be precise and use the tools as requested."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"), # This is where the agent's internal work is stored
    ]
)

