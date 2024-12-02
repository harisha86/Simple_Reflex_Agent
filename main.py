from agent import ReflexAgent
from environment import Environment

def simulate_reflex_agent():
    # Create environment and agent
    environment = Environment()
    agent = ReflexAgent()
    
    # Run simulation until environment is clean
    steps = 0
    max_steps = 10  # Prevent infinite loops
    
    print("Starting simulation...")
    print("\nInitial state:")
    environment.print_state()
    
    while not environment.is_clean() and steps < max_steps:
        steps += 1
        print(f"\nStep {steps}:")
        
        # Agent perceives environment
        perception = agent.perceive(environment.get_state())
        
        # Agent thinks and decides action
        action = agent.think(perception)
        
        # Agent acts
        performance_score = agent.act(action, environment)
        
        # Print status
        print(f"Action taken: {action}")
        environment.print_state()
        print(f"Performance score: {performance_score}")
    
    print("\nSimulation ended!")
    print(f"Steps taken: {steps}")
    print(f"Final performance score: {agent.performance_score}")
    print("Environment is clean!" if environment.is_clean() else "Could not clean environment in time!")

if __name__ == "__main__":
    simulate_reflex_agent()