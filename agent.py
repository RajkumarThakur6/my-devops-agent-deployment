import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_tool_calling_agent, AgentExecutor
from prompt import prompt

# Import all the defined tools
from tools.terraform_tool import generate_terraform_files
from tools.docker_tool import create_dockerfile
from tools.k8s_tool import generate_k8s_manifest
from tools.ci_tool import generate_ci_yaml
from tools.cd_tool import trigger_cd_pipeline

# Load environment variables from the .env file
load_dotenv()

# Initialize the Language Model (LLM)
# Using Llama 3 70b via Groq for high performance and strong reasoning.
# Temperature is set to 0 for deterministic and predictable tool usage.
llm = ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"
)

# Create a list of all the tools the agent can use
tools = [
    generate_terraform_files,
    create_dockerfile,
    generate_k8s_manifest,
    generate_ci_yaml,
    trigger_cd_pipeline,
]

# Create the tool-calling agent by combining the LLM, tools, and prompt
agent = create_tool_calling_agent(llm, tools, prompt)

# Create the Agent Executor, which is responsible for running the agent and executing tools
# `verbose=True` allows us to see the agent's thought process in the console.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
