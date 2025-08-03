from agent import agent_executor
import sys

def main():
    """Main function to run the interactive DevOps agent."""
    print("🤖 DevOps Agent is ready. Type 'exit' or 'quit' to end.")
    
    try:
        # Start an infinite loop to continuously accept user input
        while True:
            # Prompt the user for input
            query = input("You: ")
            
            # Check for exit commands
            if query.lower() in ["exit", "quit"]:
                print("🤖 Agent shutting down. Goodbye!")
                break
            
            # Skip empty input
            if not query.strip():
                continue

            # Invoke the agent executor with the user's query
            # The agent will decide which tool to call based on the input.
            result = agent_executor.invoke({"input": query})
            
            # Print the final output from the agent
            print("Agent:", result.get("output", "Sorry, I couldn't process that request."))

    except KeyboardInterrupt:
        # Handle graceful shutdown on Ctrl+C
        print("\n🤖 Agent interrupted by user. Shutting down.")
        sys.exit(0)

# Standard Python entry point
if __name__ == '__main__':
    main()
